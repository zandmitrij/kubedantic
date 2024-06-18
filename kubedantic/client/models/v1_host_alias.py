import typing as tp

from kubernetes import client

from .base import BaseKubernetesManifestObject


class V1HostAlias(BaseKubernetesManifestObject[client.V1HostAlias]):
    _kube_type = client.V1HostAlias

    hostnames: tp.Optional[tp.List[str]] = None
    ip: tp.Optional[str] = None
