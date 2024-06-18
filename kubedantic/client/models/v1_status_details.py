import typing as tp

from kubernetes import client
from pydantic import Field

from .base import BaseKubernetesManifestObject
from .v1_status_cause import V1StatusCause


class V1StatusDetails(BaseKubernetesManifestObject[client.V1StatusDetails]):
    _kube_type = client.V1StatusDetails

    causes: tp.Optional[tp.List[V1StatusCause]] = None
    group: tp.Optional[str] = None
    kind: tp.Optional[str] = None
    name: tp.Optional[str] = None
    retry_after_seconds: tp.Optional[int] = Field(None, alias='retryAfterSeconds')
    uid: tp.Optional[str] = None
