import typing as tp

from kubernetes import client
from pydantic import Field

from .base import BaseKubernetesManifestObject
from .v1_config_map_ref import V1ConfigMapRef
from .v1_secret_env_source import V1SecretEnvSource


class V1EnvFromSource(BaseKubernetesManifestObject[client.V1EnvFromSource]):
    _kube_type = client.V1EnvFromSource

    prefix: tp.Optional[str] = None
    config_map_ref: tp.Optional[V1ConfigMapRef] = Field(None, alias='configMapRef')
    secret_ref: tp.Optional[V1SecretEnvSource] = Field(None, alias='secretRef')
