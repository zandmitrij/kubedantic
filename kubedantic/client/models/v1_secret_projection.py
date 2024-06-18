import typing as tp

from kubernetes import client

from .base import BaseKubernetesManifestObject
from .v1_key_to_path import V1KeyToPath


class V1SecretProjection(BaseKubernetesManifestObject[client.V1SecretProjection]):
    _kube_type = client.V1SecretProjection

    items: tp.Optional[tp.List[V1KeyToPath]] = None
    name: tp.Optional[str] = None
    optional: tp.Optional[bool] = None
