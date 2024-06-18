import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject
from .v1_local_object_reference import V1LocalObjectReference


class V1ScaleIOVolumeSource(BaseKubernetesManifestObject[client.V1ScaleIOVolumeSource]):
    _kube_type = client.V1ScaleIOVolumeSource

    fs_type: tp.Optional[str] = Field(None, alias='fsType')
    gateway: tp.Optional[str] = None
    protection_domain: tp.Optional[str] = Field(None, alias='protectionDomain')
    read_only: tp.Optional[bool] = Field(None, alias='readOnly')
    secret_ref: tp.Optional[V1LocalObjectReference] = Field(None, alias='secretRef')
    ssl_enabled: tp.Optional[bool] = Field(None, alias='sslEnabled')
    storage_mode: tp.Optional[str] = Field(None, alias='storageMode')
    storage_pool: tp.Optional[str] = Field(None, alias='storagePool')
    system: tp.Optional[str] = None
    volume_name: tp.Optional[str] = Field(None, alias='volumeName')
