import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject


class V1ContainerPort(BaseKubernetesManifestObject[client.V1ContainerPort]):
    _kube_type = client.V1ContainerPort

    container_port: tp.Optional[int] = Field(None, alias='containerPort')
    host_ip: tp.Optional[str] = Field(None, alias='hostIP')
    host_port: tp.Optional[int] = Field(None, alias='hostPort')
    name: tp.Optional[str] = None
    protocol: tp.Optional[str] = None
