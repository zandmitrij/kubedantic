from datetime import datetime
import typing as tp

from kubernetes import client
from pydantic import Field

from .base import BaseKubernetesManifestObject


class V1JobCondition(BaseKubernetesManifestObject[client.V1JobCondition]):
    _kube_type = client.V1JobCondition

    last_probe_time: tp.Optional[datetime] = Field(None, alias='lastProbeTime')
    last_transition_time: tp.Optional[datetime] = Field(None, alias='lastTransitionTime')
    message: tp.Optional[str] = None
    reason: tp.Optional[str] = None
    status: tp.Optional[str] = None
    type: tp.Optional[str] = None
