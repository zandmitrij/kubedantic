import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject
from .v1_downward_api_volume_file import V1DownwardAPIVolumeFile


class V1DownwardAPIVolumeSource(BaseKubernetesManifestObject[client.V1DownwardAPIVolumeSource]):
    _kube_type = client.V1DownwardAPIVolumeSource

    default_mode: tp.Optional[int] = Field(None, alias='defaultMode')
    items: tp.Optional[tp.List[V1DownwardAPIVolumeFile]] = None
