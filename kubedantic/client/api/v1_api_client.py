from kubernetes import client

from kubedantic.client import models


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
