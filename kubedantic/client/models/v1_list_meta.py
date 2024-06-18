import typing as tp

from kubernetes import client
from pydantic import Field

from .base import BaseKubernetesManifestObject


class V1ListMeta(BaseKubernetesManifestObject[client.V1ListMeta]):
    _kube_type = client.V1ListMeta

    continue_: tp.Optional[str] = Field(None, validation_alias='continue', serialization_alias='_continue')
    remaining_item_count: tp.Optional[int] = Field(None, alias='remainingItemCount')
    resource_version: tp.Optional[str] = Field(None, alias='resourceVersion')
    self_link: tp.Optional[str] = Field(None, alias='selfLink')
