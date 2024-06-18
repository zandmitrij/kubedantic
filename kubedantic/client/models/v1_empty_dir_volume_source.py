import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject


class V1EmptyDirVolumeSource(BaseKubernetesManifestObject[client.V1EmptyDirVolumeSource]):
    _kube_type = client.V1EmptyDirVolumeSource

    medium: tp.Optional[str] = None
    size_limit: tp.Optional[str] = Field(None, alias='sizeLimit')
