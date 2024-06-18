import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject


class V1Toleration(BaseKubernetesManifestObject[client.V1Toleration]):
    _kube_type = client.V1Toleration

    effect: tp.Optional[str] = None
    key: tp.Optional[str] = None
    operator: tp.Optional[str] = None
    toleration_seconds: tp.Optional[int] = Field(None, alias='tolerationSeconds')
    value: tp.Optional[str] = None
