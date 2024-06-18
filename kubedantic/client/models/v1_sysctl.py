import typing as tp

from kubernetes import client

from .base import BaseKubernetesManifestObject


class V1Sysctl(BaseKubernetesManifestObject[client.V1Sysctl]):
    _kube_type = client.V1Sysctl

    name: tp.Optional[str] = None
    value: tp.Optional[str] = None
