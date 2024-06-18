import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject


class V1ContainerResizePolicy(BaseKubernetesManifestObject[client.V1ContainerResizePolicy]):
    _kube_type = client.V1ContainerResizePolicy

    resource_name: tp.Optional[str] = Field(None, alias='resourceName')
    restart_policy: tp.Optional[str] = Field(None, alias='restartPolicy')
