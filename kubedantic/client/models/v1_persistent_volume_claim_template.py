import typing as tp

from kubernetes import client

from .base import BaseKubernetesManifestObject
from .v1_object_meta import V1ObjectMeta
from .v1_persistent_volume_claim_spec import V1PersistentVolumeClaimSpec


class V1PersistentVolumeClaimTemplate(BaseKubernetesManifestObject[client.V1PersistentVolumeClaimTemplate]):
    _kube_type = client.V1PersistentVolumeClaimTemplate

    metadata: tp.Optional[V1ObjectMeta] = None
    spec: tp.Optional[V1PersistentVolumeClaimSpec] = None
