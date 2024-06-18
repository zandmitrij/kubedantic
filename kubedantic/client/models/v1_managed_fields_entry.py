import typing as tp
from datetime import datetime

from kubernetes import client
from pydantic import Field

from .base import BaseKubernetesManifestObject


class V1ManagedFieldsEntry(BaseKubernetesManifestObject[client.V1ManagedFieldsEntry]):
    _kube_type = client.V1ManagedFieldsEntry
    # TODO: check fields_v1
    api_version: tp.Optional[str] = Field(None, alias='apiVersion')
    fields_type: tp.Optional[str] = Field(None, alias='fieldsType')
    fields_v1: tp.Optional[tp.Dict] = Field(None, alias='fieldsV1')
    manager: tp.Optional[str] = None
    operation: tp.Optional[str] = None
    subresource: tp.Optional[str] = None
    time: tp.Optional[datetime] = None
