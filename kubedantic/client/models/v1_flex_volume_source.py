import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject
from .v1_local_object_reference import V1LocalObjectReference


class V1FlexVolumeSource(BaseKubernetesManifestObject[client.V1FlexVolumeSource]):
    _kube_type = client.V1FlexVolumeSource

    driver: tp.Optional[str] = None
    fs_type: tp.Optional[str] = Field(None, alias='fsType')
    options: tp.Optional[tp.Dict[str, str]] = None
    read_only: tp.Optional[bool] = Field(None, alias='readOnly')
    secret_ref: tp.Optional[V1LocalObjectReference] = Field(None, alias='secretRef')
