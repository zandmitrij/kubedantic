import typing as tp

from kubernetes import client

from .base import BaseKubernetesManifestObject


class V1NodeSelectorRequirement(BaseKubernetesManifestObject[client.V1NodeSelectorRequirement]):
    _kube_type = client.V1NodeSelectorRequirement

    key: tp.Optional[str] = None
    operator: tp.Optional[str] = None
    values: tp.Optional[tp.List[str]] = None
