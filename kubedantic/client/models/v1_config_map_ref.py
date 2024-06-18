import typing as tp

from kubernetes import client

from .base import BaseKubernetesManifestObject


class V1ConfigMapRef(BaseKubernetesManifestObject[client.V1ConfigMapEnvSource]):
    _kube_type = client.V1ConfigMapEnvSource

    name: tp.Optional[str] = None
    optional: tp.Optional[str] = None
