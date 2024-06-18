import typing as tp

from kubernetes import client
from typing_extensions import Self

from kubedantic.client import models
from .api import ClientProtocol


class Secret:
    @classmethod
    def from_file(cls, manifest: str) -> Self:
        secret = models.V1Secret.from_yaml(manifest)
        return cls(name=secret.metadata.name, namespace=secret.metadata.namespace, manifest=secret)

    @classmethod
    def from_data(
        cls,
        name: str,
        namespace: str,
        data: tp.Optional[tp.Dict[str, tp.Any]] = None,
        string_data: tp.Optional[tp.Dict[str, str]] = None,
    ) -> Self:
        if data is None and string_data is None:
            raise ValueError('data or string_data not provided')
        metadata = models.V1ObjectMeta(name=name, namespace=namespace)
        manifest = models.V1Secret(metadata=metadata, data=data, stringData=string_data)
        return cls(name=name, namespace=namespace, manifest=manifest)

    def __init__(self, name: str, namespace: str, manifest: models.V1Secret) -> None:
        self.__name = name
        self.__namespace = namespace
        self.__manifest = manifest

    @property
    def manifest(self) -> models.V1Secret:
        return self.__manifest

    @manifest.setter
    def _(self, __data: models.V1Secret) -> None:
        self.__manifest = __data

    @property
    def namespace(self) -> str:
        return self.__namespace

    @namespace.setter
    def namespace(self, __namespace: str) -> None:
        self.__namespace = __namespace
        self.__manifest.metadata.namespace = __namespace

    def create(self, client_api: ClientProtocol) -> client.V1Secret:
        return client_api.create_namespaced_secret(namespace=self.__namespace, body=self.__manifest)

    def read(self, client_api: ClientProtocol) -> client.V1Secret:
        return client_api.read_namespaced_secret(name=self.__name, namespace=self.__namespace)

    def delete(self, client_api: ClientProtocol) -> client.V1Status:
        return client_api.delete_namespaced_secret(name=self.__name, namespace=self.__namespace)
