import typing as tp

from kubernetes import client

from .base import BaseKubernetesManifestObject


class V1LabelSelectorRequirement(BaseKubernetesManifestObject[client.V1LabelSelectorRequirement]):
    _kube_type = client.V1LabelSelectorRequirement

    key: tp.Optional[str] = None
    operator: tp.Optional[str] = None
    values: tp.Optional[tp.List[str]] = None
