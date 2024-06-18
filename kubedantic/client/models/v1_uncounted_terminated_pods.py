import typing as tp

from kubernetes import client

from .base import BaseKubernetesManifestObject


class V1UncountedTerminatedPods(BaseKubernetesManifestObject[client.V1UncountedTerminatedPods]):
    _kube_type = client.V1UncountedTerminatedPods

    failed: tp.Optional[tp.List[str]] = None
    succeeded: tp.Optional[tp.List[str]] = None
