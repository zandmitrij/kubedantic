import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject


class V1VolumeDevice(BaseKubernetesManifestObject[client.V1VolumeDevice]):
    _kube_type = client.V1VolumeDevice

    device_path: tp.Optional[str] = Field(None, alias='devicePath')
    name: tp.Optional[str] = None
