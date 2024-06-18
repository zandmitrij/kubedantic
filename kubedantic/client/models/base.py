import inspect
import typing as tp

import yaml
from pydantic import BaseModel, ConfigDict
from typing_extensions import Self


T = tp.TypeVar('T')


class BaseKubernetesManifestObject(BaseModel, tp.Generic[T]):
    model_config = ConfigDict(extra='forbid')
    _kube_type: tp.ClassVar[tp.Type[T]] = dict

    @classmethod
    def from_yaml(cls, file: str) -> Self:
        with open(file, 'r') as f:
            res = yaml.safe_load(f)
        return cls(**res)

    def to_yaml(self, file: str) -> None:
        with open(file, 'w') as f:
            data = self.model_dump(exclude_none=True, by_alias=True)
            yaml.safe_dump(data, f)

    def to_yaml_str(self) -> str:
        data = self.model_dump(exclude_none=True, by_alias=True)
        return yaml.safe_dump(data, sort_keys=False)

    def model_dump_kube(self) -> T:
        if self._kube_type == dict:
            return self.model_dump(by_alias=True, exclude_defaults=True)

        res = {}
        for parameter in inspect.signature(self._kube_type.__init__).parameters:
            if parameter == 'self':
                continue
            if isinstance(field := getattr(self, parameter, None), BaseKubernetesManifestObject):
                res[parameter] = field.model_dump_kube()
            elif isinstance(field, list):
                res[parameter] = [
                    x if not isinstance(x, BaseKubernetesManifestObject) else x.model_dump_kube() for x in field
                ]
            else:
                res[parameter] = field

        return self._kube_type(**res)
