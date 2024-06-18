import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject
from .v1_container_port import V1ContainerPort
from .v1_container_resize_policy import V1ContainerResizePolicy
from .v1_env_from_source import V1EnvFromSource
from .v1_env_var import V1EnvVar
from .v1_lifecycle import V1Lifecycle
from .v1_probe import V1Probe
from .v1_resource_requiremets import V1ResourceRequirements
from .v1_security_context import V1SecurityContext
from .v1_volume_device import V1VolumeDevice
from .v1_volume_mount import V1VolumeMount


class V1EphemeralContainer(BaseKubernetesManifestObject[client.V1EphemeralContainer]):
    _kube_type = client.V1EphemeralContainer

    args: tp.Optional[tp.List[str]] = None
    command: tp.Optional[tp.List[str]] = None
    env: tp.Optional[tp.List[V1EnvVar]] = None
    env_from: tp.Optional[tp.List[V1EnvFromSource]] = Field(None, alias='envFrom')
    image: tp.Optional[str] = None
    image_pull_policy: tp.Optional[str] = Field(None, alias='imagePullPolicy')
    lifecycle: tp.Optional[V1Lifecycle] = None
    liveness_probe: tp.Optional[V1Probe] = Field(None, alias='livenessProbe')
    name: tp.Optional[str] = None
    ports: tp.Optional[tp.List[V1ContainerPort]] = None
    readiness_probe: tp.Optional[V1Probe] = Field(None, alias='readinessProbe')
    resize_policy: tp.Optional[tp.List[V1ContainerResizePolicy]] = Field(None, alias='resizePolicy')
    resources: tp.Optional[V1ResourceRequirements] = None
    restart_policy: tp.Optional[str] = Field(None, alias='restartPolicy')
    security_context: tp.Optional[V1SecurityContext] = Field(None, alias='securityContext')
    startup_probe: tp.Optional[V1Probe] = Field(None, alias='startupProbe')
    stdin: tp.Optional[bool] = None
    stdin_once: tp.Optional[bool] = Field(None, alias='stdinOnce')
    target_container_name: tp.Optional[str] = Field(None, alias='targetContainerName')
    termination_message_path: tp.Optional[str] = Field(None, alias='terminationMessagePath')
    termination_message_policy: tp.Optional[str] = Field(None, alias='terminationMessagePolicy')
    tty: tp.Optional[bool] = None
    volume_devices: tp.Optional[tp.List[V1VolumeDevice]] = Field(None, alias='volumeDevices')
    volume_mounts: tp.Optional[tp.List[V1VolumeMount]] = Field(None, alias='volumeMounts')
    working_dir: tp.Optional[str] = Field(None, alias='workingDir')
