from kubernetes import client

from kubedantic.client import models
from kubedantic.ssh_utils import decode


class V1ApiClient:
    def __init__(self, client: client.CoreV1Api) -> None:
        self._client = client

    def create_namespaced_secret(self, namespace: str, body: models.V1Secret, **kwargs) -> client.V1Secret:
        res = self._client.create_namespaced_secret(
            namespace=namespace,
            body=body.model_dump_kube(),
        )
        return res

    def read_namespaced_secret(self, name: str, namespace: str, **kwargs) -> client.V1Secret:
        res = self._client.read_namespaced_secret(
            name=name,
            namespace=namespace,
            **kwargs,
        )
        return res

    def delete_namespaced_secret(self, name: str, namespace: str, **kwargs) -> client.V1Status:
        res = self._client.delete_namespaced_secret(
            name=name,
            namespace=namespace,
            **kwargs,
        )
        return res

    def create_namespaced_config_map(self, namespace: str, body: models.V1ConfigMap, **kwargs) -> client.V1ConfigMap:
        res = self._client.create_namespaced_config_map(
            namespace=namespace,
            body=body.model_dump_kube(),
            **kwargs,
        )
        return res

    def read_namespaced_config_map(self, name: str, namespace: str, **kwargs) -> client.V1ConfigMap:
        res = self._client.read_namespaced_config_map(name=name, namespace=namespace, **kwargs)
        return res

    def delete_namespaced_config_map(self, name: str, namespace: str, **kwargs) -> str:
        res = self._client.read_namespaced_config_map(name=name, namespace=namespace, **kwargs)
        return res

    def read_namespaced_log(self, name: str, namespace: str, **kwargs) -> str:
        pods: client.V1PodList = self._client.list_namespaced_pod(namespace=namespace, **kwargs)
        # It looks like it might be created several pods for a job. Let's check out all.
        logs = []
        for pod in pods.items:
            pod_name = pod.metadata.name
            if '-'.join(pod_name.split('-')[:-1]) == name:
                request = self._client.read_namespaced_pod_log(
                    name=pod_name, namespace=namespace, _preload_content=False, **kwargs)
                # There are some decoding issues when reading model logs.
                # It looks like python cannot decode tqdm process bars using utf-8.
                # Thus, I use _preload_content=False which means we return a HTTPResponse object
                # and try to decode it myself
                log_bytes = request.read()
                request.close()  # don't forget to close the connection
                log = decode(log_bytes)
                logs.append(f"{pod_name}: {log}")
        return '\n\n'.join(logs)
