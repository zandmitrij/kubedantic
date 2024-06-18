import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject
from .v1_exec_action import V1ExecAction
from .v1_grpc_action import V1GRPCAction
from .v1_http_get_action import V1HTTPGetAction
from .v1_tcp_socket_action import V1TCPSocketAction


class V1Probe(BaseKubernetesManifestObject[client.V1Probe]):
    _kube_type = client.V1Probe

    exec_: tp.Optional[V1ExecAction] = Field(None, validation_alias='exec', serialization_alias='_exec')
    failure_threshold: tp.Optional[int] = Field(None, alias='failureThreshold')
    grpc: tp.Optional[V1GRPCAction] = None
    http_get: tp.Optional[V1HTTPGetAction] = Field(None, alias='httpGet')
    initial_delay_seconds: tp.Optional[int] = Field(None, alias='initialDelaySeconds')
    period_seconds: tp.Optional[int] = Field(None, alias='periodSeconds')
    success_threshold: tp.Optional[int] = Field(None, alias='successThreshold')
    tcp_socket: tp.Optional[V1TCPSocketAction] = Field(None, alias='tcpSocket')
    termination_grace_period_seconds: tp.Optional[int] = Field(None, alias='terminationGracePeriodSeconds')
    timeout_seconds: tp.Optional[int] = Field(None, alias='timeoutSeconds')
