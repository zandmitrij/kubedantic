import typing as tp

from kubernetes import client
from pydantic import Field

from .base import BaseKubernetesManifestObject
from .v1_object_meta import V1ObjectMeta
from .v1_job_spec import V1JobSpec
from .v1_job_status import V1JobStatus


class V1Job(BaseKubernetesManifestObject[client.V1Job]):
    _kube_type = client.V1Job

    kind: tp.Literal['Job']
    api_version: tp.Literal['batch/v1'] = Field(..., alias='apiVersion')
    metadata: V1ObjectMeta
    spec: V1JobSpec
    status: tp.Optional[V1JobStatus] = None
