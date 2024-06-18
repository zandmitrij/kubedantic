import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject
from .v1_node_selector_term import V1NodeSelectorTerm


class V1NodeSelector(BaseKubernetesManifestObject[client.V1NodeSelector]):
    _kube_type = client.V1NodeSelector

    node_selector_terms: tp.Optional[tp.List[V1NodeSelectorTerm]] = Field(None, alias='nodeSelectorTerms')
