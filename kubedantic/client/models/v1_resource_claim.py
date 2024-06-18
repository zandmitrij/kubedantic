from kubernetes import client

from .base import BaseKubernetesManifestObject


class V1ResourceClaim(BaseKubernetesManifestObject[client.V1ResourceClaim]):
    _kube_type = client.V1ResourceClaim

    name: str
