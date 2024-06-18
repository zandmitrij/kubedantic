from kubernetes import client

from kubedantic.client import models


class V1BatchApiClient:
    def __init__(self, api_client: client.BatchV1Api) -> None:
        self._client = api_client

    def create_namespaced_job(self, namespace: str, body: models.V1Job, **kwargs) -> client.V1Job:
        res = self._client.create_namespaced_job(namespace=namespace, body=body.model_dump_kube(), **kwargs)
        return res

    def read_namespaced_job(self, name: str, namespace: str, **kwargs) -> client.V1Job:
        res = self._client.read_namespaced_job(name=name, namespace=namespace, **kwargs)
        return models.V1Job.model_validate_json(res).model_dump_kube()

    def delete_namespaced_job(self, name: str, namespace: str, **kwargs) -> str:
        res = self._client.delete_namespaced_job(name=name, namespace=namespace, **kwargs)
        return res
