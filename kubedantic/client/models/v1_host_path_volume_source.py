import typing as tp

from kubernetes import client

from .base import BaseKubernetesManifestObject


class V1HostPathVolumeSource(BaseKubernetesManifestObject[client.V1HostPathVolumeSource]):
    _kube_type = client.V1HostPathVolumeSource

    path: tp.Optional[str] = None
    type: tp.Optional[str] = None
