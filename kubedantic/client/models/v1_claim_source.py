import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject


class V1ClaimSource(BaseKubernetesManifestObject[client.V1ClaimSource]):
    _kube_type = client.V1ClaimSource

    resource_claim_name: tp.Optional[str] = Field(None, alias='resourceClaimName')
    resource_claim_template_name: tp.Optional[str] = Field(None, alias='resourceClaimTemplateName')
