import typing as tp

from kubernetes import client
from pydantic import Field

from .base import BaseKubernetesManifestObject
from .v1_label_selector import V1LabelSelector
from .v1_pod_failure_policy import V1PodFailurePolicy
from .v1_pod_template_spec import V1PodTemplateSpec


class V1JobSpec(BaseKubernetesManifestObject[client.V1JobSpec]):
    _kube_type = client.V1JobSpec

    backoff_limit: int = Field(..., alias='backoffLimit')
    template: V1PodTemplateSpec
    active_deadline_seconds: tp.Optional[int] = Field(None, alias='activeDeadlineSeconds')
    completions: tp.Optional[int] = None
    parallelism: tp.Optional[int] = None
    selector: tp.Optional[V1LabelSelector] = None
    backoff_limit_per_index: tp.Optional[int] = Field(None, alias='backoffLimitPerIndex')
    completion_mode: tp.Optional[str] = Field(None, alias='completionMode')
    managed_by: tp.Optional[str] = Field(None, alias='managedBy')
    manual_selector: tp.Optional[bool] = Field(None, alias='manualSelector')
    max_failed_indexes: tp.Optional[int] = Field(None, alias='maxFailedIndexes')
    pod_replacement_policy: tp.Optional[str] = Field(None, alias='podReplacementPolicy')
    suspend: tp.Optional[bool] = None
    ttl_seconds_after_finished: tp.Optional[int] = Field(None, alias='ttlSecondsAfterFinished')
    pod_failure_policy: tp.Optional[V1PodFailurePolicy] = Field(None, alias='podFailurePolicy')
