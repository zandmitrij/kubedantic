import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject
from .v1_container import V1Container
from .v1_ephemeral_container import V1EphemeralContainer
from .v1_affinity import V1Affinity
from .v1_pod_dns_config import V1PodDNSConfig
from .v1_host_alias import V1HostAlias
from .v1_local_object_reference import V1LocalObjectReference
from .v1_pod_os import V1PodOS
from .v1_pod_readiness_gate import V1PodReadinessGate
from .v1_pod_resource_claim import V1PodResourceClaim
from .v1_pod_scheduling_gate import V1PodSchedulingGate
from .v1_pod_security_context import V1PodSecurityContext
from .v1_toleration import V1Toleration
from .v1_topology_spread_constraint import V1TopologySpreadConstraint
from .v1_volume import V1Volume


class V1PodSpec(BaseKubernetesManifestObject[client.V1PodSpec]):
    _kube_type = client.V1PodSpec

    active_deadline_seconds: tp.Optional[int] = Field(None, alias='activeDeadlineSeconds')
    affinity: tp.Optional[V1Affinity] = None
    automount_service_account_token: tp.Optional[bool] = Field(None, alias='automountServiceAccountToken')
    containers: tp.Optional[tp.List[V1Container]] = None
    dns_config: tp.Optional[V1PodDNSConfig] = Field(None, alias='dnsConfig')
    dns_policy: tp.Optional[str] = Field(None, alias='dnsPolicy')
    enable_service_links: tp.Optional[bool] = Field(None, alias='enableServiceLinks')
    ephemeral_containers: tp.Optional[tp.List[V1EphemeralContainer]] = Field(None, alias='ephemeralContainers')
    host_aliases: tp.Optional[tp.List[V1HostAlias]] = Field(None, alias='hostAliases')
    host_ipc: tp.Optional[bool] = Field(None, alias='hostIPC')
    host_network: tp.Optional[bool] = Field(None, alias='hostNetwork')
    host_pid: tp.Optional[bool] = Field(None, alias='hostPID')
    host_users: tp.Optional[bool] = Field(None, alias='hostUsers')
    hostname: tp.Optional[str] = None
    image_pull_secrets: tp.Optional[tp.List[V1LocalObjectReference]] = Field(None, alias='imagePullSecrets')
    init_containers: tp.Optional[tp.List[V1Container]] = Field(None, alias='initContainers')
    node_name: tp.Optional[str] = Field(None, alias='nodeName')
    node_selector: tp.Optional[tp.Dict[str, str]] = Field(None, alias='nodeSelector')
    os: tp.Optional[V1PodOS] = None
    overhead: tp.Optional[tp.Dict[str, str]] = None
    preemption_policy: tp.Optional[str] = Field(None, alias='preemptionPolicy')
    priority: tp.Optional[int] = None
    priority_class_name: tp.Optional[str] = Field(None, alias='priorityClassName')
    readiness_gates: tp.Optional[tp.List[V1PodReadinessGate]] = Field(None, alias='readinessGates')
    resource_claims: tp.Optional[tp.List[V1PodResourceClaim]] = Field(None, alias='resourceClaims')
    restart_policy: tp.Optional[str] = Field(None, alias='restartPolicy')
    runtime_class_name: tp.Optional[str] = Field(None, alias='runtimeClassName')
    scheduler_name: tp.Optional[str] = Field(None, alias='schedulerName')
    scheduling_gates: tp.Optional[tp.List[V1PodSchedulingGate]] = Field(None, alias='schedulingGates')
    security_context: tp.Optional[V1PodSecurityContext] = Field(None, alias='securityContext')
    service_account: tp.Optional[str] = Field(None, alias='serviceAccount')
    service_account_name: tp.Optional[str] = Field(None, alias='serviceAccountName')
    set_hostname_as_fqdn: tp.Optional[bool] = Field(None, alias='setHostnameAsFQDN')
    share_process_namespace: tp.Optional[bool] = Field(None, alias='shareProcessNamespace')
    subdomain: tp.Optional[str] = None
    termination_grace_period_seconds: tp.Optional[int] = Field(None, alias='terminationGracePeriodSeconds')
    tolerations: tp.Optional[tp.List[V1Toleration]] = None
    topology_spread_constraints: tp.Optional[tp.List[V1TopologySpreadConstraint]] = Field(
        None, alias='topologySpreadConstraints'
    )
    volumes: tp.Optional[tp.List[V1Volume]] = None
