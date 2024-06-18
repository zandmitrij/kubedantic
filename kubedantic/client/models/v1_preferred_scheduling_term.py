import typing as tp

from kubernetes import client

from .base import BaseKubernetesManifestObject
from .v1_node_selector_term import V1NodeSelectorTerm


class V1PreferredSchedulingTerm(BaseKubernetesManifestObject[client.V1PreferredSchedulingTerm]):
    _kube_type = client.V1PreferredSchedulingTerm

    preference: tp.Optional[V1NodeSelectorTerm] = None
    weight: tp.Optional[int] = None
