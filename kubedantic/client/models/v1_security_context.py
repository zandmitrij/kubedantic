import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject
from .v1_capabilities import V1Capabilities
from .v1_se_linux_options import V1SELinuxOptions
from .v1_seccomp_profile import V1SeccompProfile
from .v1_windows_security_context_options import V1WindowsSecurityContextOptions


class V1SecurityContext(BaseKubernetesManifestObject[client.V1SecurityContext]):
    _kube_type = client.V1SecurityContext

    allow_privilege_escalation: tp.Optional[bool] = Field(None, alias='allowPrivilegeEscalation')
    capabilities: tp.Optional[V1Capabilities] = None
    privileged: tp.Optional[bool] = None
    proc_mount: tp.Optional[str] = Field(None, alias='procMount')
    read_only_root_filesystem: tp.Optional[bool] = Field(None, alias='readOnlyRootFilesystem')
    run_as_group: tp.Optional[int] = Field(None, alias='runAsGroup')
    run_as_non_root: tp.Optional[bool] = Field(None, alias='runAsNonRoot')
    run_as_user: tp.Optional[int] = Field(None, alias='runAsUser')
    se_linux_options: tp.Optional[V1SELinuxOptions] = Field(None, alias='seLinuxOptions')
    seccomp_profile: tp.Optional[V1SeccompProfile] = Field(None, alias='seccompProfile')
    windows_options: tp.Optional[V1WindowsSecurityContextOptions] = Field(None, alias='windowsOptions')
