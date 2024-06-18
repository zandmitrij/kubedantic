import typing as tp

from kubernetes import client

from .base import BaseKubernetesManifestObject
from .v1_object_meta import V1ObjectMeta
from .v1_pod_spec import V1PodSpec


class V1PodTemplateSpec(BaseKubernetesManifestObject[client.V1PodTemplateSpec]):
    _kube_type = client.V1PodTemplateSpec

    spec: V1PodSpec
    metadata: tp.Optional[V1ObjectMeta] = None
