import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject
from .v1_aws_elastic_block_store_volume_source import V1AWSElasticBlockStoreVolumeSource
from .v1_azure_disk_volume_source import V1AzureDiskVolumeSource
from .v1_azure_file_volume_source import V1AzureFileVolumeSource
from .v1_ceph_fs_volume_source import V1CephFSVolumeSource
from .v1_cinder_volume_source import V1CinderVolumeSource
from .v1_config_map_volume_source import V1ConfigMapVolumeSource
from .v1_csi_volume_source import V1CSIVolumeSource
from .v1_downward_api_volume_source import V1DownwardAPIVolumeSource
from .v1_empty_dir_volume_source import V1EmptyDirVolumeSource
from .v1_ephemeral_volume_source import V1EphemeralVolumeSource
from .v1_fc_volume_source import V1FCVolumeSource
from .v1_flex_volume_source import V1FlexVolumeSource
from .v1_flocker_volume_source import V1FlockerVolumeSource
from .v1_gce_persistent_disk_volume_source import V1GCEPersistentDiskVolumeSource
from .v1_git_repo_volume_source import V1GitRepoVolumeSource
from .v1_glusterfs_volume_source import V1GlusterfsVolumeSource
from .v1_host_path_volume_source import V1HostPathVolumeSource
from .v1_iscsi_volume_source import V1ISCSIVolumeSource
from .v1_nfs_volume_source import V1NFSVolumeSource
from .v1_persistent_volume_claim_volume_source import V1PersistentVolumeClaimVolumeSource
from .v1_photon_persistent_disk_volume_source import V1PhotonPersistentDiskVolumeSource
from .v1_portworx_volume_source import V1PortworxVolumeSource
from .v1_projected_volume_source import V1ProjectedVolumeSource
from .v1_quobyte_volume_source import V1QuobyteVolumeSource
from .v1_rbd_volume_source import V1RBDVolumeSource
from .v1_scale_io_volume_source import V1ScaleIOVolumeSource
from .v1_secret_volume_source import V1SecretVolumeSource
from .v1_storage_os_volume_source import V1StorageOSVolumeSource
from .v1_vsphere_virtual_disk_volume_source import V1VsphereVirtualDiskVolumeSource


class V1Volume(BaseKubernetesManifestObject[client.V1Volume]):
    _kube_type = client.V1Volume

    aws_elastic_block_store: tp.Optional[V1AWSElasticBlockStoreVolumeSource] = Field(None, alias='awsElasticBlockStore')
    azure_disk: tp.Optional[V1AzureDiskVolumeSource] = Field(None, alias='azureDisk')
    azure_file: tp.Optional[V1AzureFileVolumeSource] = Field(None, alias='azureFile')
    cephfs: tp.Optional[V1CephFSVolumeSource] = None
    cinder: tp.Optional[V1CinderVolumeSource] = None
    config_map: tp.Optional[V1ConfigMapVolumeSource] = Field(None, alias='configMap')
    csi: tp.Optional[V1CSIVolumeSource] = None
    downward_api: tp.Optional[V1DownwardAPIVolumeSource] = Field(None, alias='downwardAPI')
    empty_dir: tp.Optional[V1EmptyDirVolumeSource] = Field(None, alias='emptyDir')
    ephemeral: tp.Optional[V1EphemeralVolumeSource] = None
    fc: tp.Optional[V1FCVolumeSource] = None
    flex_volume: tp.Optional[V1FlexVolumeSource] = Field(None, alias='flexVolume')
    flocker: tp.Optional[V1FlockerVolumeSource] = None
    gce_persistent_disk: tp.Optional[V1GCEPersistentDiskVolumeSource] = Field(None, alias='gcePersistentDisk')
    git_repo: tp.Optional[V1GitRepoVolumeSource] = Field(None, alias='gitRepo')
    glusterfs: tp.Optional[V1GlusterfsVolumeSource] = None
    host_path: tp.Optional[V1HostPathVolumeSource] = Field(None, alias='hostPath')
    iscsi: tp.Optional[V1ISCSIVolumeSource] = None
    name: tp.Optional[str] = None
    nfs: tp.Optional[V1NFSVolumeSource] = None
    persistent_volume_claim: tp.Optional[V1PersistentVolumeClaimVolumeSource] = Field(
        None, alias='persistentVolumeClaim'
    )
    photon_persistent_disk: tp.Optional[V1PhotonPersistentDiskVolumeSource] = Field(None, alias='photonPersistentDisk')
    portworx_volume: tp.Optional[V1PortworxVolumeSource] = Field(None, alias='portworxVolume')
    projected: tp.Optional[V1ProjectedVolumeSource] = None
    quobyte: tp.Optional[V1QuobyteVolumeSource] = None
    rbd: tp.Optional[V1RBDVolumeSource] = None
    scale_io: tp.Optional[V1ScaleIOVolumeSource] = Field(None, alias='scaleIO')
    secret: tp.Optional[V1SecretVolumeSource] = None
    storageos: tp.Optional[V1StorageOSVolumeSource] = None
    vsphere_volume: tp.Optional[V1VsphereVirtualDiskVolumeSource] = Field(None, alias='vsphereVolume')
