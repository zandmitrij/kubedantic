import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject
from .v1_key_to_path import V1KeyToPath


class V1ConfigMapVolumeSource(BaseKubernetesManifestObject[client.V1ConfigMapVolumeSource]):
    _kube_type = client.V1ConfigMapVolumeSource

    default_mode: tp.Optional[int] = Field(None, alias='defaultMode')
    items: tp.Optional[tp.List[V1KeyToPath]] = None
    name: tp.Optional[str] = None
    optional: tp.Optional[bool] = None
