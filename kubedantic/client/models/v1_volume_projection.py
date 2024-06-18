import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject
from .v1_cluster_trust_bundle_projection import V1ClusterTrustBundleProjection
from .v1_config_map_projection import V1ConfigMapProjection
from .v1_downward_api_projection import V1DownwardAPIProjection
from .v1_secret_projection import V1SecretProjection
from .v1_service_account_token_projection import V1ServiceAccountTokenProjection


class V1VolumeProjection(BaseKubernetesManifestObject[client.V1VolumeProjection]):
    _kube_type = client.V1VolumeProjection

    cluster_trust_bundle: tp.Optional[V1ClusterTrustBundleProjection] = Field(None, alias='clusterTrustBundle')
    config_map: tp.Optional[V1ConfigMapProjection] = Field(None, alias='configMap')
    downward_api: tp.Optional[V1DownwardAPIProjection] = Field(None, alias='downwardAPI')
    secret: tp.Optional[V1SecretProjection] = None
    service_account_token: tp.Optional[V1ServiceAccountTokenProjection] = Field(None, alias='serviceAccountToken')
