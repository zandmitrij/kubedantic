import typing as tp

from kubernetes import client

from .base import BaseKubernetesManifestObject


class V1StatusCause(BaseKubernetesManifestObject[client.V1StatusCause]):
    _kube_type = client.V1StatusCause

    field: tp.Optional[str] = None
    message: tp.Optional[str] = None
    reason: tp.Optional[str] = None
