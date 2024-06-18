import typing as tp

from kubernetes import client

from .base import BaseKubernetesManifestObject


class V1SecretEnvSource(BaseKubernetesManifestObject[client.V1SecretEnvSource]):
    _kube_type = client.V1SecretEnvSource

    name: tp.Optional[str] = None
    optional: tp.Optional[str] = None
