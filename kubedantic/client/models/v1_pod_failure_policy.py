import typing as tp

from kubernetes import client

from .base import BaseKubernetesManifestObject

from .v1_pod_failure_policy_rule import V1PodFailurePolicyRule


class V1PodFailurePolicy(BaseKubernetesManifestObject[client.V1PodFailurePolicy]):
    _kube_type = client.V1PodFailurePolicy

    rules: tp.List[V1PodFailurePolicyRule]
