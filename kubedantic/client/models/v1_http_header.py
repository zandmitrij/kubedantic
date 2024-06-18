import typing as tp

from kubernetes import client

from .base import BaseKubernetesManifestObject


class V1HTTPHeader(BaseKubernetesManifestObject[client.V1HTTPHeader]):
    _kube_type = client.V1HTTPHeader

    name: tp.Optional[str] = None
    value: tp.Optional[str] = None
