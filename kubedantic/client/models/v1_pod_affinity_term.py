import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject
from .v1_label_selector import V1LabelSelector


class V1PodAffinityTerm(BaseKubernetesManifestObject[client.V1PodAffinityTerm]):
    _kube_type = client.V1PodAffinityTerm

    label_selector: tp.Optional[V1LabelSelector] = Field(None, alias='labelSelector')
    match_label_keys: tp.Optional[tp.List[str]] = Field(None, alias='matchLabelKeys')
    mismatch_label_keys: tp.Optional[tp.List[str]] = Field(None, alias='mismatchLabelKeys')
    namespace_selector: tp.Optional[V1LabelSelector] = Field(None, alias='namespaceSelector')
    namespaces: tp.Optional[tp.List[str]] = None
    topology_key: tp.Optional[str] = Field(None, alias='topologyKey')
