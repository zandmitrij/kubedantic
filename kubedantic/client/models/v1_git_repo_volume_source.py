import typing as tp

from kubernetes import client

from .base import BaseKubernetesManifestObject


class V1GitRepoVolumeSource(BaseKubernetesManifestObject[client.V1GitRepoVolumeSource]):
    _kube_type = client.V1GitRepoVolumeSource

    directory: tp.Optional[str] = None
    repository: tp.Optional[str] = None
    revision: tp.Optional[str] = None
