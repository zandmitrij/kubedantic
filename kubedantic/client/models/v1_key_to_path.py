import typing as tp

from kubernetes import client

from .base import BaseKubernetesManifestObject


class V1KeyToPath(BaseKubernetesManifestObject[client.V1KeyToPath]):
    _kube_type = client.V1KeyToPath

    key: tp.Optional[str] = None
    mode: tp.Optional[int] = None
    path: tp.Optional[str] = None
