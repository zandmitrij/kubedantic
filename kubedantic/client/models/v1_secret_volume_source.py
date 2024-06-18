import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject
from .v1_key_to_path import V1KeyToPath


class V1SecretVolumeSource(BaseKubernetesManifestObject[client.V1SecretVolumeSource]):
    _kube_type = client.V1SecretVolumeSource

    default_mode: tp.Optional[int] = Field(None, alias='defaultMode')
    items: tp.Optional[tp.List[V1KeyToPath]] = None
    optional: tp.Optional[bool] = None
    secret_name: tp.Optional[str] = Field(None, alias='secretName')
