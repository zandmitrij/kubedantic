import typing as tp

from kubernetes import client
from pydantic import Field

from .base import BaseKubernetesManifestObject
from .v1_label_selector_requirement import V1LabelSelectorRequirement


class V1LabelSelector(BaseKubernetesManifestObject[client.V1LabelSelector]):
    _kube_type = client.V1LabelSelector

    match_expressions: tp.Optional[tp.List[V1LabelSelectorRequirement]] = Field(None, alias='matchExpressions')
    match_labels: tp.Optional[tp.Dict[str, str]] = Field(None, alias='matchLabels')
