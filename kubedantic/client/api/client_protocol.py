import typing as tp

from kubernetes import client

from kubedantic.client import models


class ClientProtocol(tp.Protocol):
    def create_namespaced_secret(namespace: str, body: models.V1Secret, **kwargs) -> client.V1Secret:
        pass

    def read_namespaced_secret(name: str, namespace: str, **kwargs) -> client.V1Secret:
        pass

    def delete_namespaced_secret(name: str, namespace: str, **kwargs) -> client.V1Status:
        pass

    def create_namespaced_config_map(self, namespace: str, body: models.V1ConfigMap, **kwargs) -> client.V1ConfigMap:
        pass

    def read_namespaced_config_map(self, name: str, namespace: str, **kwargs) -> client.V1ConfigMap:
        pass

    def delete_namespaced_config_map(self, name: str, namespace: str, **kwargs) -> client.V1Status:
        pass
