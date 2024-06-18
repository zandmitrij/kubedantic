import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject


class V1FlockerVolumeSource(BaseKubernetesManifestObject[client.V1FlockerVolumeSource]):
    _kube_type = client.V1FlockerVolumeSource

    dataset_name: tp.Optional[str] = Field(None, alias='datasetName')
    dataset_uuid: tp.Optional[str] = Field(None, alias='datasetUUID')
