import typing as tp

from .field import Field


def get_typing(v: str) -> str:
    return v.replace('list', 'tp.List').replace('dict(str, str)', 'tp.Dict[str, str]')


def get_field(k: str, model) -> str:
    x = model.attribute_map[k]
    if x == k:
        return 'None'
    return f"Field(None, alias='{x}')"


class Model(tp.NamedTuple):
    name: str
    fields: tp.List[Field]

    def __str__(self) -> str:
        res = f'class {self.name}(BaseKubernetesManifestObject[client.{self.name}]):\n'
        res += f'    _kube_type = client.{self.name}\n\n'
        for field in self.fields:
            res += f'    {field}\n'
        return res

    @classmethod
    def create(cls, __model):
        fields = []
        for name, type_ in __model.openapi_types.items():
            typing = get_typing(type_)
            value = get_field(name, __model)
            fields.append(Field(name, typing, value))
        return cls(name=__model.__name__, fields=fields)
