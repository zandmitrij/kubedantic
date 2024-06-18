import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject
from .v1_node_selector_requirement import V1NodeSelectorRequirement


class V1NodeSelectorTerm(BaseKubernetesManifestObject[client.V1NodeSelectorTerm]):
    _kube_type = client.V1NodeSelectorTerm

    match_expressions: tp.Optional[tp.List[V1NodeSelectorRequirement]] = Field(None, alias='matchExpressions')
    match_fields: tp.Optional[tp.List[V1NodeSelectorRequirement]] = Field(None, alias='matchFields')
