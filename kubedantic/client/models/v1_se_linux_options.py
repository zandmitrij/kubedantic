import typing as tp

from kubernetes import client

from .base import BaseKubernetesManifestObject


class V1SELinuxOptions(BaseKubernetesManifestObject[client.V1SELinuxOptions]):
    _kube_type = client.V1SELinuxOptions

    level: tp.Optional[str] = None
    role: tp.Optional[str] = None
    type: tp.Optional[str] = None
    user: tp.Optional[str] = None
