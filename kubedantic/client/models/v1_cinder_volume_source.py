import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject
from .v1_local_object_reference import V1LocalObjectReference


class V1CinderVolumeSource(BaseKubernetesManifestObject[client.V1CinderVolumeSource]):
    _kube_type = client.V1CinderVolumeSource

    fs_type: tp.Optional[str] = Field(None, alias='fsType')
    read_only: tp.Optional[bool] = Field(None, alias='readOnly')
    secret_ref: tp.Optional[V1LocalObjectReference] = Field(None, alias='secretRef')
    volume_id: tp.Optional[str] = Field(None, alias='volumeID')
