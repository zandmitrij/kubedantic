import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject


class V1FCVolumeSource(BaseKubernetesManifestObject[client.V1FCVolumeSource]):
    _kube_type = client.V1FCVolumeSource

    fs_type: tp.Optional[str] = Field(None, alias='fsType')
    lun: tp.Optional[int] = None
    read_only: tp.Optional[bool] = Field(None, alias='readOnly')
    target_ww_ns: tp.Optional[tp.List[str]] = Field(None, alias='targetWWNs')
    wwids: tp.Optional[tp.List[str]] = None
