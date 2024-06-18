import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject
from .v1_http_header import V1HTTPHeader


class V1HTTPGetAction(BaseKubernetesManifestObject[client.V1HTTPGetAction]):
    _kube_type = client.V1HTTPGetAction

    host: tp.Optional[str] = None
    http_headers: tp.Optional[tp.List[V1HTTPHeader]] = Field(None, alias='httpHeaders')
    path: tp.Optional[str] = None
    port: tp.Optional[object] = None
    scheme: tp.Optional[str] = None
