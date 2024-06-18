from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject


class V1AzureDiskVolumeSource(BaseKubernetesManifestObject[client.V1AzureDiskVolumeSource]):
    _kube_type = client.V1AzureDiskVolumeSource

    caching_mode: str = Field(None, alias='cachingMode')
    disk_name: str = Field(None, alias='diskName')
    disk_uri: str = Field(None, alias='diskURI')
    fs_type: str = Field(None, alias='fsType')
    kind: str = None
    read_only: bool = Field(None, alias='readOnly')
