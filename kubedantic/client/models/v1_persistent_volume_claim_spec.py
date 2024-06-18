import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject
from .v1_typed_local_object_reference import V1TypedLocalObjectReference
from .v1_typed_object_reference import V1TypedObjectReference
from .v1_volume_resource_requirements import V1VolumeResourceRequirements
from .v1_label_selector import V1LabelSelector


class V1PersistentVolumeClaimSpec(BaseKubernetesManifestObject[client.V1PersistentVolumeClaimSpec]):
    _kube_type = client.V1PersistentVolumeClaimSpec

    access_modes: tp.Optional[tp.List[str]] = Field(None, alias='accessModes')
    data_source: tp.Optional[V1TypedLocalObjectReference] = Field(None, alias='dataSource')
    data_source_ref: tp.Optional[V1TypedObjectReference] = Field(None, alias='dataSourceRef')
    resources: tp.Optional[V1VolumeResourceRequirements] = None
    selector: tp.Optional[V1LabelSelector] = None
    storage_class_name: tp.Optional[str] = Field(None, alias='storageClassName')
    volume_attributes_class_name: tp.Optional[str] = Field(None, alias='volumeAttributesClassName')
    volume_mode: tp.Optional[str] = Field(None, alias='volumeMode')
    volume_name: tp.Optional[str] = Field(None, alias='volumeName')
