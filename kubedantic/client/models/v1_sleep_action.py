import typing as tp

from kubernetes import client

from .base import BaseKubernetesManifestObject


class V1SleepAction(BaseKubernetesManifestObject[client.V1SleepAction]):
    _kube_type = client.V1SleepAction

    seconds: tp.Optional[int] = None
