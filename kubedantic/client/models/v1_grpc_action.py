import typing as tp

from kubernetes import client

from .base import BaseKubernetesManifestObject


class V1GRPCAction(BaseKubernetesManifestObject[client.V1GRPCAction]):
    _kube_type = client.V1GRPCAction

    port: tp.Optional[int] = None
    service: tp.Optional[str] = None
