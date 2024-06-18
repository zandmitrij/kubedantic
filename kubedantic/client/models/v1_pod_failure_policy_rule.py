import typing as tp

from kubernetes import client
from pydantic import Field

from .base import BaseKubernetesManifestObject
from .v1_pod_failure_policy_on_exit_codes_requirement import V1PodFailurePolicyOnExitCodesRequirement
from .v1_pod_failure_policy_on_pod_conditions_pattern import V1PodFailurePolicyOnPodConditionsPattern


class V1PodFailurePolicyRule(BaseKubernetesManifestObject[client.V1PodFailurePolicyRule]):
    _kube_type = client.V1PodFailurePolicyRule

    action: str
    on_exit_codes: tp.Optional[V1PodFailurePolicyOnExitCodesRequirement] = Field(None, alias='onExitCodes')
    on_pod_conditions: tp.Optional[tp.List[V1PodFailurePolicyOnPodConditionsPattern]] = Field(
        None, alias='onPodConditions'
    )
