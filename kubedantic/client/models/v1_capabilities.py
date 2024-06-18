import typing as tp

from kubernetes import client

from .base import BaseKubernetesManifestObject


class V1Capabilities(BaseKubernetesManifestObject[client.V1Capabilities]):
    _kube_type = client.V1Capabilities

    add: tp.Optional[tp.List[str]] = None
    drop: tp.Optional[tp.List[str]] = None
