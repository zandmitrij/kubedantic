import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject


class V1PortworxVolumeSource(BaseKubernetesManifestObject[client.V1PortworxVolumeSource]):
    _kube_type = client.V1PortworxVolumeSource

    fs_type: tp.Optional[str] = Field(None, alias='fsType')
    read_only: tp.Optional[bool] = Field(None, alias='readOnly')
    volume_id: tp.Optional[str] = Field(None, alias='volumeID')
