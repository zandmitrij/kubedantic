from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject


class V1AWSElasticBlockStoreVolumeSource(BaseKubernetesManifestObject[client.V1AWSElasticBlockStoreVolumeSource]):
    _kube_type = client.V1AWSElasticBlockStoreVolumeSource

    fs_type: str = Field(None, alias='fsType')
    partition: int = None
    read_only: bool = Field(None, alias='readOnly')
    volume_id: str = Field(None, alias='volumeID')
