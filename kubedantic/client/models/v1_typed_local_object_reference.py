import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject


class V1TypedLocalObjectReference(BaseKubernetesManifestObject[client.V1TypedLocalObjectReference]):
    _kube_type = client.V1TypedLocalObjectReference

    api_group: tp.Optional[str] = Field(None, alias='apiGroup')
    kind: tp.Optional[str] = None
    name: tp.Optional[str] = None
