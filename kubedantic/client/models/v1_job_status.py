from datetime import datetime
import typing as tp

from kubernetes import client
from pydantic import Field

from .base import BaseKubernetesManifestObject
from .v1_job_condition import V1JobCondition
from .v1_uncounted_terminated_pods import V1UncountedTerminatedPods


class V1JobStatus(BaseKubernetesManifestObject[client.V1JobStatus]):
    _kube_type = client.V1JobStatus

    active: tp.Optional[int] = None
    completed_indexes: tp.Optional[str] = Field(None, alias='completedIndexes')
    completion_time: tp.Optional[datetime] = Field(None, alias='completionTime')
    conditions: tp.Optional[tp.List[V1JobCondition]] = None
    failed: tp.Optional[int] = None
    failed_indexes: tp.Optional[str] = Field(None, alias='failedIndexes')
    ready: tp.Optional[int] = None
    start_time: tp.Optional[datetime] = Field(None, alias='startTime')
    succeeded: tp.Optional[int] = None
    terminating: tp.Optional[int] = None
    uncounted_terminated_pods: tp.Optional[V1UncountedTerminatedPods] = Field(None, alias='uncountedTerminatedPods')
