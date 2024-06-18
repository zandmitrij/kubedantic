import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject
from .v1_persistent_volume_claim_template import V1PersistentVolumeClaimTemplate


class V1EphemeralVolumeSource(BaseKubernetesManifestObject[client.V1EphemeralVolumeSource]):
    _kube_type = client.V1EphemeralVolumeSource

    volume_claim_template: tp.Optional[V1PersistentVolumeClaimTemplate] = Field(None, alias='volumeClaimTemplate')
