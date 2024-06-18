import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject


class V1GCEPersistentDiskVolumeSource(BaseKubernetesManifestObject[client.V1GCEPersistentDiskVolumeSource]):
    _kube_type = client.V1GCEPersistentDiskVolumeSource

    fs_type: tp.Optional[str] = Field(None, alias='fsType')
    partition: tp.Optional[int] = None
    pd_name: tp.Optional[str] = Field(None, alias='pdName')
    read_only: tp.Optional[bool] = Field(None, alias='readOnly')
