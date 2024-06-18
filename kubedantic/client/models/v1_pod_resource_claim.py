import typing as tp

from kubernetes import client

from .base import BaseKubernetesManifestObject
from .v1_claim_source import V1ClaimSource


class V1PodResourceClaim(BaseKubernetesManifestObject[client.V1PodResourceClaim]):
    _kube_type = client.V1PodResourceClaim

    name: tp.Optional[str] = None
    source: tp.Optional[V1ClaimSource] = None
