from kubernetes import client

from kubedantic.ssh_utils import SshClient
from kubedantic.client import models


class SshBatchClient:
    def __init__(self, ssh_client: SshClient) -> None:
        self.ssh_client = ssh_client

    def run_command(self, command: str, raise_error: bool = True) -> str:
        with self.ssh_client as ssh_client:
            return ssh_client.run_command(command, raise_error=raise_error)

    def create_namespaced_job(self, namespace: str, body: models.V1Job, **kwargs) -> client.V1Job:
        x = body.to_yaml_str().replace('$', '\$')
        command = f"""echo "{x}" | kubectl create -n {namespace} -o json -f -"""
        res = self.run_command(command)
        print(res)
        return models.V1Job.model_validate_json(res).model_dump_kube()

    def read_namespaced_job(self, name: str, namespace: str, **kwargs) -> client.V1Job:
        command = f"kubectl get job {name} --namespace={namespace} -o json"
        res = self.run_command(command)
        return models.V1Job.model_validate_json(res).model_dump_kube()

    def delete_namespaced_job(self, name: str, namespace: str, **kwargs) -> str:
        command = f"kubectl delete job {name} --namespace={namespace}"
        res = self.run_command(command)
        return res
