import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject
from .v1_label_selector import V1LabelSelector


class V1TopologySpreadConstraint(BaseKubernetesManifestObject[client.V1TopologySpreadConstraint]):
    _kube_type = client.V1TopologySpreadConstraint

    label_selector: tp.Optional[V1LabelSelector] = Field(None, alias='labelSelector')
    match_label_keys: tp.Optional[tp.List[str]] = Field(None, alias='matchLabelKeys')
    max_skew: tp.Optional[int] = Field(None, alias='maxSkew')
    min_domains: tp.Optional[int] = Field(None, alias='minDomains')
    node_affinity_policy: tp.Optional[str] = Field(None, alias='nodeAffinityPolicy')
    node_taints_policy: tp.Optional[str] = Field(None, alias='nodeTaintsPolicy')
    topology_key: tp.Optional[str] = Field(None, alias='topologyKey')
    when_unsatisfiable: tp.Optional[str] = Field(None, alias='whenUnsatisfiable')
