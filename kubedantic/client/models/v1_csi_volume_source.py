import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject
from .v1_local_object_reference import V1LocalObjectReference


class V1CSIVolumeSource(BaseKubernetesManifestObject[client.V1CSIVolumeSource]):
    _kube_type = client.V1CSIVolumeSource

    driver: tp.Optional[str] = None
    fs_type: tp.Optional[str] = Field(None, alias='fsType')
    node_publish_secret_ref: tp.Optional[V1LocalObjectReference] = Field(None, alias='nodePublishSecretRef')
    read_only: tp.Optional[bool] = Field(None, alias='readOnly')
    volume_attributes: tp.Optional[tp.Dict[str, str]] = Field(None, alias='volumeAttributes')
