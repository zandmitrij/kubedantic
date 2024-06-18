import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject


class V1VolumeMount(BaseKubernetesManifestObject[client.V1VolumeMount]):
    _kube_type = client.V1VolumeMount

    mount_path: tp.Optional[str] = Field(None, alias='mountPath')
    mount_propagation: tp.Optional[str] = Field(None, alias='mountPropagation')
    name: tp.Optional[str] = None
    read_only: tp.Optional[bool] = Field(None, alias='readOnly')
    recursive_read_only: tp.Optional[str] = Field(None, alias='recursiveReadOnly')
    sub_path: tp.Optional[str] = Field(None, alias='subPath')
    sub_path_expr: tp.Optional[str] = Field(None, alias='subPathExpr')
