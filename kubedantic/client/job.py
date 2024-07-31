import time

from kubernetes import client, watch
from typing_extensions import Self

from kubedantic.client import models
from .api import ClientProtocol, BatchClientProtocol


class Job:
    @classmethod
    def from_file(cls, manifest: str) -> Self:
        job = models.V1Job.from_yaml(manifest)
        return cls(name=job.metadata.name, namespace=job.metadata.namespace, manifest=job)

    def __init__(self, name: str, namespace: str, manifest: models.V1Job) -> None:
        self.name = name
        self.__namespace = namespace
        self.__manifest = manifest
        self.__label_selector = None

    @property
    def label_selector(self) -> str:
        if self.__label_selector is None:
            x = models.V1LabelSelector(matchLabels=self.__manifest.metadata.labels).model_dump_kube()
            self.__label_selector = ','.join(f'{k}={v}' for k, v in x.match_labels.items())
        return self.__label_selector

    @property
    def namespace(self) -> str:
        return self.__namespace

    @namespace.setter
    def namespace(self, __namespace: str) -> None:
        self.__namespace = __namespace
        self.__manifest.metadata.namespace = __namespace

    def delete(self, client_api: client.BatchV1Api) -> str:
        options = client.V1DeleteOptions(propagation_policy='Foreground', grace_period_seconds=5)
        api_response: client.V1Status = client_api.delete_namespaced_job(
            name=self.name,
            namespace=self.__namespace,
            body=options,
        )
        return api_response

    def read_pod_logs(self, client_api: ClientProtocol) -> str:
        return client_api.read_namespaced_log(name=self.name, namespace=self.__namespace)

    def create(self, client_api: BatchClientProtocol) -> client.V1Job:
        api_response = client_api.create_namespaced_job(namespace=self.__namespace, body=self.__manifest)
        return api_response.status

    def get_status(self, client_api: client.BatchV1Api) -> client.V1JobStatus:
        api_response: client.V1Job = client_api.read_namespaced_job(name=self.name, namespace=self.__namespace)
        return api_response.status

    def run(
        self,
        client_api: ClientProtocol,
        job_client_api: client.BatchV1Api,
        delete_after: bool = False,
        delay: int = 5,
    ) -> None:
        status = self.create(job_client_api)
        print(f"Job created. status='{status}'")

        while not (status.succeeded is not None or status.failed is not None):
            status = self.get_status(job_client_api)
            time.sleep(delay)

        if delete_after:
            delete_status = self.delete(job_client_api)
            print(f"Job {self.name} deleted. status='{delete_status}'")
        else:
            print(f"Job {self.name} finished. {status = }")

        if status.failed:
            raise RuntimeError("Job has failed. Please see logs to learn more.")
