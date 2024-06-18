import typing as tp

from kubernetes import client

from .base import BaseKubernetesManifestObject
from .v1_pod_dns_config_option import V1PodDNSConfigOption


class V1PodDNSConfig(BaseKubernetesManifestObject[client.V1PodDNSConfig]):
    _kube_type = client.V1PodDNSConfig

    nameservers: tp.Optional[tp.List[str]] = None
    options: tp.Optional[tp.List[V1PodDNSConfigOption]] = None
    searches: tp.Optional[tp.List[str]] = None
