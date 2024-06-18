import typing as tp

from kubernetes import client
from pydantic import Field

from .base import BaseKubernetesManifestObject


class V1PodFailurePolicyOnExitCodesRequirement(
    BaseKubernetesManifestObject[client.V1PodFailurePolicyOnExitCodesRequirement]
):
    _kube_type = client.V1PodFailurePolicyOnExitCodesRequirement

    container_name: str = Field(..., alias='containerName')
    operator: str
    values: tp.List[int]
