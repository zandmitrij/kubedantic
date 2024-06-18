import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject


class V1ResourceFieldSelector(BaseKubernetesManifestObject[client.V1ResourceFieldSelector]):
    _kube_type = client.V1ResourceFieldSelector

    container_name: tp.Optional[str] = Field(None, alias='containerName')
    divisor: tp.Optional[str] = None
    resource: tp.Optional[str] = None
