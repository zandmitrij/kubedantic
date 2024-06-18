import typing as tp

from kubernetes import client

from .base import BaseKubernetesManifestObject


class V1TCPSocketAction(BaseKubernetesManifestObject[client.V1TCPSocketAction]):
    _kube_type = client.V1TCPSocketAction

    host: tp.Optional[str] = None
    port: tp.Optional[object] = None
