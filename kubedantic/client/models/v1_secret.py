import typing as tp
import base64

from kubernetes import client
from pydantic import Field, field_serializer, model_serializer

from .base import BaseKubernetesManifestObject
from .v1_object_meta import V1ObjectMeta


def b64encode(__s: str):
    return base64.b64encode(bytes(__s, 'utf-8')).decode('utf-8')


class V1Secret(BaseKubernetesManifestObject[client.V1Secret]):
    _kube_type = client.V1Secret

    kind: tp.Literal['Secret'] = 'Secret'
    api_version: tp.Literal['v1'] = Field('v1', alias='apiVersion')
    metadata: V1ObjectMeta
    data: tp.Optional[tp.Dict[str, str]] = None
    string_data: tp.Optional[tp.Dict[str, tp.Optional[str]]] = Field(None, alias='stringData')
    immutable: tp.Optional[bool] = None
    type: tp.Literal['Opaque'] = 'Opaque'

    @field_serializer('string_data')
    def serialize_data(string_data: tp.Optional[tp.Dict[str, tp.Optional[str]]]) -> tp.Optional[str]:
        return {k: str(v) for k, v in string_data.items()} if string_data is not None else None

    @model_serializer
    def ser(self):
        data = {**self.data} if self.data is not None else {}
        if self.string_data is not None:
            data.update(**{k: b64encode(v) for k, v in self.string_data.items()})
        return {
            'kind': self.kind,
            'apiVersion': self.api_version,
            'metadata': self.metadata.model_dump(exclude_none=True, by_alias=True),
            'data': data,
            'immutable': self.immutable,
            'type': self.type,
        }
