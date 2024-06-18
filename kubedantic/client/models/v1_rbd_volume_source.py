import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject
from .v1_local_object_reference import V1LocalObjectReference


class V1RBDVolumeSource(BaseKubernetesManifestObject[client.V1RBDVolumeSource]):
    _kube_type = client.V1RBDVolumeSource

    fs_type: tp.Optional[str] = Field(None, alias='fsType')
    image: tp.Optional[str] = None
    keyring: tp.Optional[str] = None
    monitors: tp.Optional[tp.List[str]] = None
    pool: tp.Optional[str] = None
    read_only: tp.Optional[bool] = Field(None, alias='readOnly')
    secret_ref: tp.Optional[V1LocalObjectReference] = Field(None, alias='secretRef')
    user: tp.Optional[str] = None
