import typing as tp

from kubernetes import client

from .base import BaseKubernetesManifestObject
from .v1_downward_api_volume_file import V1DownwardAPIVolumeFile


class V1DownwardAPIProjection(BaseKubernetesManifestObject[client.V1DownwardAPIProjection]):
    _kube_type = client.V1DownwardAPIProjection

    items: tp.Optional[tp.List[V1DownwardAPIVolumeFile]] = None
