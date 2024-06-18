import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject
from .v1_se_linux_options import V1SELinuxOptions
from .v1_seccomp_profile import V1SeccompProfile
from .v1_windows_security_context_options import V1WindowsSecurityContextOptions
from .v1_sysctl import V1Sysctl


class V1PodSecurityContext(BaseKubernetesManifestObject[client.V1PodSecurityContext]):
    _kube_type = client.V1PodSecurityContext

    fs_group: tp.Optional[int] = Field(None, alias='fsGroup')
    fs_group_change_policy: tp.Optional[str] = Field(None, alias='fsGroupChangePolicy')
    run_as_group: tp.Optional[int] = Field(None, alias='runAsGroup')
    run_as_non_root: tp.Optional[bool] = Field(None, alias='runAsNonRoot')
    run_as_user: tp.Optional[int] = Field(None, alias='runAsUser')
    se_linux_options: tp.Optional[V1SELinuxOptions] = Field(None, alias='seLinuxOptions')
    seccomp_profile: tp.Optional[V1SeccompProfile] = Field(None, alias='seccompProfile')
    supplemental_groups: tp.Optional[tp.List[int]] = Field(None, alias='supplementalGroups')
    sysctls: tp.Optional[tp.List[V1Sysctl]] = None
    windows_options: tp.Optional[V1WindowsSecurityContextOptions] = Field(None, alias='windowsOptions')
