import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject
from .v1_node_selector import V1NodeSelector
from .v1_preferred_scheduling_term import V1PreferredSchedulingTerm


class V1NodeAffinity(BaseKubernetesManifestObject[client.V1NodeAffinity]):
    _kube_type = client.V1NodeAffinity

    preferred_during_scheduling_ignored_during_execution: tp.Optional[tp.List[V1PreferredSchedulingTerm]] = Field(
        None, alias='preferredDuringSchedulingIgnoredDuringExecution'
    )
    required_during_scheduling_ignored_during_execution: tp.Optional[V1NodeSelector] = Field(
        None, alias='requiredDuringSchedulingIgnoredDuringExecution'
    )
