import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject
from .v1_config_map_key_selector import V1ConfigMapKeySelector
from .v1_object_field_selector import V1ObjectFieldSelector
from .v1_resource_field_selector import V1ResourceFieldSelector
from .v1_secret_key_selector import V1SecretKeySelector


class V1EnvVarSource(BaseKubernetesManifestObject[client.V1EnvVarSource]):
    _kube_type = client.V1EnvVarSource

    config_map_key_ref: tp.Optional[V1ConfigMapKeySelector] = Field(None, alias='configMapKeyRef')
    field_ref: tp.Optional[V1ObjectFieldSelector] = Field(None, alias='fieldRef')
    resource_field_ref: tp.Optional[V1ResourceFieldSelector] = Field(None, alias='resourceFieldRef')
    secret_key_ref: tp.Optional[V1SecretKeySelector] = Field(None, alias='secretKeyRef')
