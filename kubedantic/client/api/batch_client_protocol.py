import typing as tp

from kubernetes import client

from kubedantic.client import models


class BatchClientProtocol(tp.Protocol):
    def create_namespaced_job(self, namespace: str, body: models.V1Job, **kwargs) -> client.V1Job:
        pass

    def read_namespaced_job(self, name: str, namespace: str, **kwargs) -> client.V1Job:
        pass
