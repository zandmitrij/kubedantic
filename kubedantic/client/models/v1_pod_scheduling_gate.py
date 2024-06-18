import typing as tp

from kubernetes import client

from .base import BaseKubernetesManifestObject


class V1PodSchedulingGate(BaseKubernetesManifestObject[client.V1PodSchedulingGate]):
    _kube_type = client.V1PodSchedulingGate

    name: tp.Optional[str] = None
