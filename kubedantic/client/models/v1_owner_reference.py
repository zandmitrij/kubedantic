import typing as tp

from kubernetes import client
from pydantic import Field

from .base import BaseKubernetesManifestObject


class V1OwnerReference(BaseKubernetesManifestObject[client.V1OwnerReference]):
    _kube_type = client.V1OwnerReference

    api_version: tp.Optional[str] = Field(None, alias='apiVersion')
    name: tp.Optional[str] = None
    uid: tp.Optional[str] = None
    kind: tp.Optional[str] = None
    controller: tp.Optional[bool] = None
    block_owner_deletion: tp.Optional[bool] = Field(None, alias='blockOwnerDeletion')
