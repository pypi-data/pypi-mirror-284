import logging
import os
from typing import Any, Dict, List, Tuple, TypeVar, Union, cast

import lightning as L
import torch
from torch import nn
from transformers import CLIPModel, CLIPProcessor, CLIPVisionModel

from fusion_bench.mixins.lightning_fabric import LightningFabricMixin
from fusion_bench.modelpool import ModelPool
from fusion_bench.modelpool.huggingface_clip_vision import HuggingFaceClipVisionPool
from fusion_bench.models.hf_clip import HFCLIPClassifier
from fusion_bench.tasks.clip_classification import get_classnames_and_templates
from fusion_bench.utils import timeit_context

log = logging.getLogger(__name__)

TensorOrModule = TypeVar("TensorOrModule", torch.Tensor, torch.nn.Module, Any)


class CLIPClassificationMixin(LightningFabricMixin):
    """
    This mixin provides methods to classify images using the CLIP model.
    """

    _clip_processor: CLIPProcessor = None
    # a dict of zeroshot weights for each task, each key is the task name
    zeroshot_weights: Dict[str, torch.Tensor] = {}

    def __init__(self):
        super().__init__()

    @property
    def clip_processor(self):
        if self._clip_processor is None:
            raise ValueError(
                f"CLIP processor is not initialized. "
                "Call `self.setup_zero_shot_classification_head` to initialize it and the classification head."
            )
        else:
            return self._clip_processor

    def setup_zero_shot_classification_head(self):
        self.modelpool = cast(HuggingFaceClipVisionPool, self.modelpool)
        clip_model_config = self.modelpool.get_model_config("_pretrained_")

        with timeit_context("Loading CLIP processor and pretrained CLIP model."):
            self._clip_processor = CLIPProcessor.from_pretrained(clip_model_config.path)
            clip_model = CLIPModel.from_pretrained(clip_model_config.path)
            clip_classifier = HFCLIPClassifier(clip_model, self._clip_processor)
            self.visual_projection = clip_model.visual_projection.requires_grad_(False)
            self.logit_scale = clip_model.logit_scale.exp()
            self.visual_projection = self.to_device(self.visual_projection)
            self.logit_scale = self.to_device(self.logit_scale)

        cache_dir = cache_file = os.path.join(
            self.config.cache_dir,
            os.path.normpath(f"{os.path.basename(clip_model_config.path)}"),
        )
        if not os.path.exists(cache_dir):
            log.info(
                f"Creating cache directory for zero-shot classification head at {cache_dir}"
            )
            os.makedirs(cache_dir)
        log.info(f"cache directory for zero-shot classification head: {cache_dir}")
        for task in self.modelpool.model_names:
            if self.fabric.is_global_zero:
                cache_file = os.path.join(
                    cache_dir, os.path.normpath(f"{task}_zeroshot_weights.pt")
                )
                if os.path.exists(cache_file):
                    log.info(f"Loading cached zeroshot weights for task: {task}")
                    zeroshot_weights = torch.load(cache_file, map_location="cpu")
                else:
                    log.info(
                        f"Construct zero shot classification head for task: {task}"
                    )
                    classnames, templates = get_classnames_and_templates(
                        self.modelpool.get_train_dataset_config(task)["dataset"].name
                    )
                    clip_classifier.set_classification_task(classnames, templates)
                    zeroshot_weights = clip_classifier.zeroshot_weights
                    log.info(f"save zeroshot weights to {cache_file}")
                    torch.save(zeroshot_weights, cache_file)

            self.fabric.barrier()
            self.zeroshot_weights[task] = self.fabric.broadcast(zeroshot_weights, src=0)
            self.zeroshot_weights[task] = self.to_device(self.zeroshot_weights[task])

    def compute_logits(
        self,
        module: Union[nn.Module, CLIPVisionModel],
        images: torch.Tensor,
        task: str,
    ) -> torch.Tensor:
        text_embeds = self.zeroshot_weights[task]

        image_embeds = module(images)[1]
        image_embeds = self.visual_projection(image_embeds)

        # normalize embeddings
        image_embeds = image_embeds / image_embeds.norm(p=2, dim=-1, keepdim=True)

        # cosine similarity
        logits_per_text = torch.matmul(text_embeds, image_embeds.t()) * self.logit_scale
        logits_per_image = logits_per_text.t()

        return logits_per_image
