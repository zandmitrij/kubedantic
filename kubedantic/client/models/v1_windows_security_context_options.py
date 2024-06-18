import typing as tp

from pydantic import Field
from kubernetes import client

from .base import BaseKubernetesManifestObject


class V1WindowsSecurityContextOptions(BaseKubernetesManifestObject[client.V1WindowsSecurityContextOptions]):
    _kube_type = client.V1WindowsSecurityContextOptions

    gmsa_credential_spec: tp.Optional[str] = Field(None, alias='gmsaCredentialSpec')
    gmsa_credential_spec_name: tp.Optional[str] = Field(None, alias='gmsaCredentialSpecName')
    host_process: tp.Optional[bool] = Field(None, alias='hostProcess')
    run_as_user_name: tp.Optional[str] = Field(None, alias='runAsUserName')
