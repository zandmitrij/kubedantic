import os
import re
import typing as tp

from typing_extensions import Self

from .constants import BUILTINS
from .model import Model


def get_module_name(__model_name: str):
    filename = __model_name.replace('V1', '')
    return re.sub(r'(?<!^)(?=[A-Z])', '_', filename).lower()


class Module(tp.NamedTuple):
    name: str
    imports: tp.List[str]
    model: Model
    folder: str = 'kubedantic/validation'

    def exists(self) -> bool:
        return os.path.exists(os.path.join(self.folder, f'v1_{self.name}.py'))

    def __str__(self) -> str:
        imports = '\n'.join(self.imports)
        return f'{imports}\n\n\n{self.model}'

    def write(self):
        if self.exists():
            return
        with open(f'{self.folder}/test_{self.name}.py', 'w') as f:
            f.write(str(self))

    @classmethod
    def from_model(cls, __model, known_models: tp.Set[str]) -> Self:
        imports = [
            'import typing as tp\n',
            'from pydantic import Field',
            'from kubernetes import client\n',
            'from .base import BaseKubernetesManifestObject',
        ]

        model = Model.create(__model)

        for field in model.fields:
            if field.type_hint in BUILTINS:
                continue
            if field.type_hint in known_models:
                continue
            module_name = get_module_name(field.type_hint)
            known_models.add(module_name)
            with open('new_model.txt', 'a') as f:
                f.write(f'        client.{field.type_hint},')
                f.write('\n')
            imports.append(f'from .v1_{module_name} import {field.type_hint}')

        return cls(
            name=get_module_name(__model.__name__),
            imports=imports,
            model=model,
        )
