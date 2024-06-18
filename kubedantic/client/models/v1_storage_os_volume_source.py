import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject
from .v1_local_object_reference import V1LocalObjectReference


class V1StorageOSVolumeSource(BaseKubernetesManifestObject[client.V1StorageOSVolumeSource]):
    _kube_type = client.V1StorageOSVolumeSource

    fs_type: tp.Optional[str] = Field(None, alias='fsType')
    read_only: tp.Optional[bool] = Field(None, alias='readOnly')
    secret_ref: tp.Optional[V1LocalObjectReference] = Field(None, alias='secretRef')
    volume_name: tp.Optional[str] = Field(None, alias='volumeName')
    volume_namespace: tp.Optional[str] = Field(None, alias='volumeNamespace')
