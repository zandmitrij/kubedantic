import typing as tp

from kubernetes import client

from .base import BaseKubernetesManifestObject


class V1VolumeResourceRequirements(BaseKubernetesManifestObject[client.V1VolumeResourceRequirements]):
    _kube_type = client.V1VolumeResourceRequirements

    limits: tp.Optional[tp.Dict[str, str]] = None
    requests: tp.Optional[tp.Dict[str, str]] = None
