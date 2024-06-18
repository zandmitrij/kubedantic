import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject
from .v1_label_selector import V1LabelSelector


class V1ClusterTrustBundleProjection(BaseKubernetesManifestObject[client.V1ClusterTrustBundleProjection]):
    _kube_type = client.V1ClusterTrustBundleProjection

    label_selector: tp.Optional[V1LabelSelector] = Field(None, alias='labelSelector')
    name: tp.Optional[str] = None
    optional: tp.Optional[bool] = None
    path: tp.Optional[str] = None
    signer_name: tp.Optional[str] = Field(None, alias='signerName')
