from kubernetes import client
from typing_extensions import Self

from . import models as models
from .api import ClientProtocol


class ConfigMap:
    @classmethod
    def from_file(cls, manifest: str) -> Self:
        config_map = models.V1ConfigMap.from_yaml(manifest)
        return cls(name=config_map.metadata.name, namespace=config_map.metadata.namespace, manifest=config_map)

    def __init__(self, name: str, namespace: str, manifest: models.V1ConfigMap) -> None:
        self.__name = name
        self.__namespace = namespace
        self.__manifest = manifest
        self.__label_selector = None

    @property
    def label_selector(self) -> client.V1LabelSelector:
        if self.__label_selector is None:
            self.__label_selector = models.V1LabelSelector(
                matchLabels=self.__manifest.metadata.labels
            ).model_dump_kube()
        return self.__label_selector

    @property
    def namespace(self) -> str:
        return self.__namespace

    @namespace.setter
    def namespace(self, __namespace: str) -> None:
        self.__namespace = __namespace
        self.__manifest.metadata.namespace = __namespace

    def create(self, client_api: ClientProtocol) -> client.V1ConfigMap:
        return client_api.create_namespaced_config_map(namespace=self.__namespace, body=self.__manifest)

    def read(self, client_api: ClientProtocol) -> client.V1ConfigMap:
        return client_api.read_namespaced_config_map(name=self.__name, namespace=self.__namespace)

    def delete(self, client_api: ClientProtocol) -> client.V1Status:
        return client_api.delete_namespaced_config_map(name=self.__name, namespace=self.__namespace)
