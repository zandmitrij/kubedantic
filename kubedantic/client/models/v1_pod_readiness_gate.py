import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject


class V1PodReadinessGate(BaseKubernetesManifestObject[client.V1PodReadinessGate]):
    _kube_type = client.V1PodReadinessGate

    condition_type: tp.Optional[str] = Field(None, alias='conditionType')
