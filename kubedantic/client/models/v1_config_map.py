import typing as tp

from kubernetes import client
from pydantic import Field

from .base import BaseKubernetesManifestObject
from .v1_object_meta import V1ObjectMeta


class V1ConfigMap(BaseKubernetesManifestObject[client.V1ConfigMap]):
    _kube_type = client.V1ConfigMap

    kind: tp.Literal['ConfigMap']
    api_version: tp.Literal['v1'] = Field(..., alias='apiVersion')
    metadata: V1ObjectMeta
    data: tp.Optional[tp.Dict[str, str]] = None
    binary_data: tp.Optional[tp.Dict[str, str]] = Field(None, alias='binaryData')
    immutable: tp.Optional[bool] = None
