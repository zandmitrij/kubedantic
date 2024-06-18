import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject


class V1VsphereVirtualDiskVolumeSource(BaseKubernetesManifestObject[client.V1VsphereVirtualDiskVolumeSource]):
    _kube_type = client.V1VsphereVirtualDiskVolumeSource

    fs_type: tp.Optional[str] = Field(None, alias='fsType')
    storage_policy_id: tp.Optional[str] = Field(None, alias='storagePolicyID')
    storage_policy_name: tp.Optional[str] = Field(None, alias='storagePolicyName')
    volume_path: tp.Optional[str] = Field(None, alias='volumePath')
