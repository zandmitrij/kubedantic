import typing as tp

from kubernetes import client

from .base import BaseKubernetesManifestObject


class V1PodDNSConfigOption(BaseKubernetesManifestObject[client.V1PodDNSConfigOption]):
    _kube_type = client.V1PodDNSConfigOption

    name: tp.Optional[str] = None
    value: tp.Optional[str] = None
