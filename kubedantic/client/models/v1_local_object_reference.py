import typing as tp

from kubernetes import client

from .base import BaseKubernetesManifestObject


class V1LocalObjectReference(BaseKubernetesManifestObject[client.V1LocalObjectReference]):
    _kube_type = client.V1LocalObjectReference

    name: tp.Optional[str] = None
