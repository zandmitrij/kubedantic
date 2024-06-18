import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject
from .v1_lifecycle_handler import V1LifecycleHandler


class V1Lifecycle(BaseKubernetesManifestObject[client.V1Lifecycle]):
    _kube_type = client.V1Lifecycle

    post_start: tp.Optional[V1LifecycleHandler] = Field(None, alias='postStart')
    pre_stop: tp.Optional[V1LifecycleHandler] = Field(None, alias='preStop')
