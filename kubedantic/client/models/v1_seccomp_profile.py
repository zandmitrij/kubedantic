import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject


class V1SeccompProfile(BaseKubernetesManifestObject[client.V1SeccompProfile]):
    _kube_type = client.V1SeccompProfile

    localhost_profile: tp.Optional[str] = Field(None, alias='localhostProfile')
    type: tp.Optional[str] = None
