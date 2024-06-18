import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject


class V1QuobyteVolumeSource(BaseKubernetesManifestObject[client.V1QuobyteVolumeSource]):
    _kube_type = client.V1QuobyteVolumeSource

    group: tp.Optional[str] = None
    read_only: tp.Optional[bool] = Field(None, alias='readOnly')
    registry: tp.Optional[str] = None
    tenant: tp.Optional[str] = None
    user: tp.Optional[str] = None
    volume: tp.Optional[str] = None
