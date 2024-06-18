from kubernetes import client

from .base import BaseKubernetesManifestObject


class V1PodFailurePolicyOnPodConditionsPattern(
    BaseKubernetesManifestObject[client.V1PodFailurePolicyOnPodConditionsPattern]
):
    _kube_type = client.V1PodFailurePolicyOnPodConditionsPattern

    status: str
    type: str
