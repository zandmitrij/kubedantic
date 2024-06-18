import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject


class V1GlusterfsVolumeSource(BaseKubernetesManifestObject[client.V1GlusterfsVolumeSource]):
    _kube_type = client.V1GlusterfsVolumeSource

    endpoints: tp.Optional[str] = None
    path: tp.Optional[str] = None
    read_only: tp.Optional[bool] = Field(None, alias='readOnly')
