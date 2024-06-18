import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject
from .v1_local_object_reference import V1LocalObjectReference


class V1CephFSVolumeSource(BaseKubernetesManifestObject[client.V1CephFSVolumeSource]):
    _kube_type = client.V1CephFSVolumeSource

    monitors: tp.Optional[tp.List[str]] = None
    path: tp.Optional[str] = None
    read_only: tp.Optional[bool] = Field(None, alias='readOnly')
    secret_file: tp.Optional[str] = Field(None, alias='secretFile')
    secret_ref: tp.Optional[V1LocalObjectReference] = Field(None, alias='secretRef')
    user: tp.Optional[str] = None
