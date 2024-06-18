import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject


class V1PersistentVolumeClaimVolumeSource(BaseKubernetesManifestObject[client.V1PersistentVolumeClaimVolumeSource]):
    _kube_type = client.V1PersistentVolumeClaimVolumeSource

    claim_name: tp.Optional[str] = Field(None, alias='claimName')
    read_only: tp.Optional[bool] = Field(None, alias='readOnly')
