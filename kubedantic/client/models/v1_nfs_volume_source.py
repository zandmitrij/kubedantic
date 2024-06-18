import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject


class V1NFSVolumeSource(BaseKubernetesManifestObject[client.V1NFSVolumeSource]):
    _kube_type = client.V1NFSVolumeSource

    path: tp.Optional[str] = None
    read_only: tp.Optional[bool] = Field(None, alias='readOnly')
    server: tp.Optional[str] = None
