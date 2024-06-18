import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject
from .v1_object_field_selector import V1ObjectFieldSelector
from .v1_resource_field_selector import V1ResourceFieldSelector


class V1DownwardAPIVolumeFile(BaseKubernetesManifestObject[client.V1DownwardAPIVolumeFile]):
    _kube_type = client.V1DownwardAPIVolumeFile

    field_ref: tp.Optional[V1ObjectFieldSelector] = Field(None, alias='fieldRef')
    mode: tp.Optional[int] = None
    path: tp.Optional[str] = None
    resource_field_ref: tp.Optional[V1ResourceFieldSelector] = Field(None, alias='resourceFieldRef')
