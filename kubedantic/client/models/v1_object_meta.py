import typing as tp
from datetime import datetime

from kubernetes import client
from pydantic import Field

from .base import BaseKubernetesManifestObject
from .v1_managed_fields_entry import V1ManagedFieldsEntry
from .v1_owner_reference import V1OwnerReference


class V1ObjectMeta(BaseKubernetesManifestObject[client.V1ObjectMeta]):
    _kube_type = client.V1ObjectMeta

    name: tp.Optional[str] = None
    namespace: tp.Optional[str] = None
    labels: tp.Optional[tp.Dict[str, str]] = None
    annotations: tp.Optional[tp.Dict[str, str]] = None
    creation_timestamp: tp.Optional[datetime] = Field(None, alias='creationTimestamp')
    deletion_grace_period_seconds: tp.Optional[int] = Field(None, alias='deletionGracePeriodSeconds')
    deletion_timestamp: tp.Optional[datetime] = Field(None, alias='deletionTimestamp')
    finalizers: tp.Optional[tp.List[str]] = None
    generate_name: tp.Optional[str] = Field(None, alias='generateName')
    resource_version: tp.Optional[str] = Field(None, alias='resourceVersion')
    generation: tp.Optional[int] = None
    self_link: tp.Optional[str] = Field(None, alias='selfLink')
    uid: tp.Optional[str] = None
    managed_fields: tp.Optional[tp.List[V1ManagedFieldsEntry]] = Field(None, alias='managedFields')
    owner_references: tp.Optional[tp.List[V1OwnerReference]] = Field(None, alias='ownerReferences')
