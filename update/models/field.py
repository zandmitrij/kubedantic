import typing as tp


class Field(tp.NamedTuple):
    name: str
    type_hint: str
    value: str

    def __str__(self) -> str:
        return f'{self.name}: tp.Optional[{self.type_hint}] = {self.value}'
