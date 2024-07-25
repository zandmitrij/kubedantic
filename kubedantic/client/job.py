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

    def read_pod_logs(self, client_api: client.CoreV1Api) -> None:
        pods: client.V1PodList = client_api.list_namespaced_pod(
            namespace=self.__namespace, label_selector=self.label_selector
        )
        # It looks like it might be created several pods for a job. Let's check out all.
        for pod in pods.items:
            pod_name = pod.metadata.name

            w = watch.Watch()
            for request in w.stream(
                    client_api.read_namespaced_pod_log,
                    name=pod_name, namespace=self.__namespace, follow=True, _preload_content=False):
                # There are some decoding issues when reading model logs.
                # It looks like python cannot decode tqdm process bars using utf-8.
                # Thus, I use _preload_content=False which means we return a HTTPResponse object
                # and try to decode it myself
                log_bytes = request.read()
                request.close()  # don't forget to close the connection
                try:
                    log = log_bytes.decode("utf-8")
                except UnicodeDecodeError:
                    try:
                        log = log_bytes.decode('cp737')
                    except UnicodeDecodeError:
                        log = str(log_bytes)
                print(f"{pod_name}: {log}")

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

        # self.read_pod_logs(client_api)

        while not (status.succeeded is not None or status.failed is not None):
            status = self.get_status(job_client_api)
            time.sleep(delay)

        if delete_after:
            status = self.delete(job_client_api)
            print(f"Job {self.name} deleted. status='{status}'")
        else:
            print(f"Job {self.name} finished. {status = }")
