import typing as tp

from kubernetes import client

from .base import BaseKubernetesManifestObject


class V1PodOS(BaseKubernetesManifestObject[client.V1PodOS]):
    _kube_type = client.V1PodOS

    name: tp.Optional[str] = None
