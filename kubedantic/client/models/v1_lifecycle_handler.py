import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject
from .v1_exec_action import V1ExecAction
from .v1_http_get_action import V1HTTPGetAction
from .v1_tcp_socket_action import V1TCPSocketAction
from .v1_sleep_action import V1SleepAction


class V1LifecycleHandler(BaseKubernetesManifestObject[client.V1LifecycleHandler]):
    _kube_type = client.V1LifecycleHandler

    exec_: tp.Optional[V1ExecAction] = Field(None, validation_alias='exec', serialization_alias='_exec')
    http_get: tp.Optional[V1HTTPGetAction] = Field(None, alias='httpGet')
    sleep: tp.Optional[V1SleepAction] = None
    tcp_socket: tp.Optional[V1TCPSocketAction] = Field(None, alias='tcpSocket')
