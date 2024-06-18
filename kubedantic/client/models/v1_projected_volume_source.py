import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject
from .v1_volume_projection import V1VolumeProjection


class V1ProjectedVolumeSource(BaseKubernetesManifestObject[client.V1ProjectedVolumeSource]):
    _kube_type = client.V1ProjectedVolumeSource

    default_mode: tp.Optional[int] = Field(None, alias='defaultMode')
    sources: tp.Optional[tp.List[V1VolumeProjection]] = None
