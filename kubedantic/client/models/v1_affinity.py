import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject
from .v1_node_affinity import V1NodeAffinity
from .v1_pod_affinity import V1PodAffinity
from .v1_pod_anti_affinity import V1PodAntiAffinity


class V1Affinity(BaseKubernetesManifestObject[client.V1Affinity]):
    _kube_type = client.V1Affinity

    node_affinity: tp.Optional[V1NodeAffinity] = Field(None, alias='nodeAffinity')
    pod_affinity: tp.Optional[V1PodAffinity] = Field(None, alias='podAffinity')
    pod_anti_affinity: tp.Optional[V1PodAntiAffinity] = Field(None, alias='podAntiAffinity')
