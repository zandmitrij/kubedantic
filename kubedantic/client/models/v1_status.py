import typing as tp

from kubernetes import client
from pydantic import Field

from .base import BaseKubernetesManifestObject
from .v1_status_details import V1StatusDetails
from .v1_list_meta import V1ListMeta


class V1Status(BaseKubernetesManifestObject[client.V1Status]):
    _kube_type = client.V1Status

    api_version: tp.Optional[str] = Field(None, alias='apiVersion')
    code: tp.Optional[int] = None
    details: tp.Optional[V1StatusDetails] = None
    kind: tp.Optional[str] = None
    message: tp.Optional[str] = None
    metadata: tp.Optional[V1ListMeta] = None
    reason: tp.Optional[str] = None
    status: tp.Optional[str] = None
