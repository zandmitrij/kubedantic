from kubernetes import client

from kubedantic.ssh_utils import SshClient
from kubedantic.client import models


class SShApiClient:
    def __init__(self, client: SshClient):
        self.ssh_client = client

    def run_command(self, command: str) -> str:
        with self.ssh_client as ssh_client:
            return ssh_client.run_command(command)

    def _create(self, namespace: str, body: str, **kwargs) -> str:
        command = f"""echo "{body}" | kubectl create -n {namespace} -o json -f -"""
        return self.run_command(command)

    def create_namespaced_secret(self, namespace: str, body: models.V1Secret, **kwargs) -> client.V1Secret:
        res = self._create(namespace, body.to_yaml_str(), **kwargs)
        return models.V1Secret.model_validate_json(res).model_dump_kube()

    def read_namespaced_secret(self, name: str, namespace: str, **kwargs) -> client.V1Secret:
        command = f"kubectl get secret {name} --namespace={namespace} -o json"
        res = self.run_command(command)
        return models.V1Secret.model_validate_json(res).model_dump_kube()

    def delete_namespaced_secret(self, name: str, namespace: str, **kwargs) -> client.V1Status:
        command = f"kubectl delete secret {name} --namespace={namespace}"
        return self.run_command(command)

    def create_namespaced_config_map(self, namespace: str, body: models.V1ConfigMap, **kwargs) -> client.V1ConfigMap:
        res = self._create(namespace, body.to_yaml_str(), **kwargs)
        return models.V1ConfigMap.model_validate_json(res).model_dump_kube()

    def read_namespaced_config_map(self, name: str, namespace: str, **kwargs) -> client.V1ConfigMap:
        command = f"kubectl get cm {name} --namespace={namespace} -o json"
        res = self.run_command(command)
        return models.V1ConfigMap.model_validate_json(res).model_dump_kube()

    def delete_namespaced_config_map(self, name: str, namespace: str, **kwargs) -> str:
        command = f"kubectl delete cm {name} --namespace={namespace} "
        return self.run_command(command)
