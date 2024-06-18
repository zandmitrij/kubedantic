import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject


class V1TypedObjectReference(BaseKubernetesManifestObject[client.V1TypedObjectReference]):
    _kube_type = client.V1TypedObjectReference

    api_group: tp.Optional[str] = Field(None, alias='apiGroup')
    kind: tp.Optional[str] = None
    name: tp.Optional[str] = None
    namespace: tp.Optional[str] = None
