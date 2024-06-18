import typing as tp

from kubernetes import client

from .base import BaseKubernetesManifestObject


class V1SecretKeySelector(BaseKubernetesManifestObject[client.V1SecretKeySelector]):
    _kube_type = client.V1SecretKeySelector

    key: tp.Optional[str] = None
    name: tp.Optional[str] = None
    optional: tp.Optional[bool] = None
