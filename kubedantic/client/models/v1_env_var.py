import typing as tp

from pydantic import Field
from kubernetes import client
from .base import BaseKubernetesManifestObject
from .v1_env_var_source import V1EnvVarSource


class V1EnvVar(BaseKubernetesManifestObject[client.V1EnvVar]):
    _kube_type = client.V1EnvVar

    name: tp.Optional[str] = None
    value: tp.Optional[str] = None
    value_from: tp.Optional[V1EnvVarSource] = Field(None, alias='valueFrom')
