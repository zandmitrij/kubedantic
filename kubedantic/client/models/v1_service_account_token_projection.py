import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject


class V1ServiceAccountTokenProjection(BaseKubernetesManifestObject[client.V1ServiceAccountTokenProjection]):
    _kube_type = client.V1ServiceAccountTokenProjection

    audience: tp.Optional[str] = None
    expiration_seconds: tp.Optional[int] = Field(None, alias='expirationSeconds')
    path: tp.Optional[str] = None
