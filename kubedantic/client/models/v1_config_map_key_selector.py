import typing as tp

from kubernetes import client

from .base import BaseKubernetesManifestObject


class V1ConfigMapKeySelector(BaseKubernetesManifestObject[client.V1ConfigMapKeySelector]):
    _kube_type = client.V1ConfigMapKeySelector

    key: tp.Optional[str] = None
    name: tp.Optional[str] = None
    optional: tp.Optional[bool] = None
