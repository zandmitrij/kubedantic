import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject
from .v1_pod_affinity_term import V1PodAffinityTerm


class V1WeightedPodAffinityTerm(BaseKubernetesManifestObject[client.V1WeightedPodAffinityTerm]):
    _kube_type = client.V1WeightedPodAffinityTerm

    pod_affinity_term: tp.Optional[V1PodAffinityTerm] = Field(None, alias='podAffinityTerm')
    weight: tp.Optional[int] = None
