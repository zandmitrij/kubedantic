import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject
from .v1_local_object_reference import V1LocalObjectReference


class V1ISCSIVolumeSource(BaseKubernetesManifestObject[client.V1ISCSIVolumeSource]):
    _kube_type = client.V1ISCSIVolumeSource

    chap_auth_discovery: tp.Optional[bool] = Field(None, alias='chapAuthDiscovery')
    chap_auth_session: tp.Optional[bool] = Field(None, alias='chapAuthSession')
    fs_type: tp.Optional[str] = Field(None, alias='fsType')
    initiator_name: tp.Optional[str] = Field(None, alias='initiatorName')
    iqn: tp.Optional[str] = None
    iscsi_interface: tp.Optional[str] = Field(None, alias='iscsiInterface')
    lun: tp.Optional[int] = None
    portals: tp.Optional[tp.List[str]] = None
    read_only: tp.Optional[bool] = Field(None, alias='readOnly')
    secret_ref: tp.Optional[V1LocalObjectReference] = Field(None, alias='secretRef')
    target_portal: tp.Optional[str] = Field(None, alias='targetPortal')
