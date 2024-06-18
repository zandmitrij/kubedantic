import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject


class V1ObjectFieldSelector(BaseKubernetesManifestObject[client.V1ObjectFieldSelector]):
    _kube_type = client.V1ObjectFieldSelector

    api_version: tp.Optional[str] = Field(None, alias='apiVersion')
    field_path: tp.Optional[str] = Field(None, alias='fieldPath')
