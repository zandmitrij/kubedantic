import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject


class V1AzureFileVolumeSource(BaseKubernetesManifestObject[client.V1AzureFileVolumeSource]):
    _kube_type = client.V1AzureFileVolumeSource

    read_only: tp.Optional[bool] = Field(None, alias='readOnly')
    secret_name: tp.Optional[str] = Field(None, alias='secretName')
    share_name: tp.Optional[str] = Field(None, alias='shareName')
