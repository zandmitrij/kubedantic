import typing as tp

from kubernetes import client

from .base import BaseKubernetesManifestObject


class V1ExecAction(BaseKubernetesManifestObject[client.V1ExecAction]):
    _kube_type = client.V1ExecAction

    command: tp.Optional[tp.List[str]] = None
