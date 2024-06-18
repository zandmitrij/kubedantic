import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject
from .v1_pod_affinity_term import V1PodAffinityTerm
from .v1_weighted_pod_affinity_term import V1WeightedPodAffinityTerm


class V1PodAntiAffinity(BaseKubernetesManifestObject[client.V1PodAntiAffinity]):
    _kube_type = client.V1PodAntiAffinity

    preferred_during_scheduling_ignored_during_execution: tp.Optional[tp.List[V1WeightedPodAffinityTerm]] = Field(
        None, alias='preferredDuringSchedulingIgnoredDuringExecution'
    )
    required_during_scheduling_ignored_during_execution: tp.Optional[tp.List[V1PodAffinityTerm]] = Field(
        None, alias='requiredDuringSchedulingIgnoredDuringExecution'
    )
