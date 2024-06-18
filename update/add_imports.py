import re
import typing as tp
from pathlib import Path


def extract_class_name(file_path: Path):
    with open(file_path, 'r') as file:
        file_content = file.read()

    class_pattern = re.compile(r'class\s+(\w+)\s*\(BaseKubernetesManifestObject\[client\.\w+\]\)\s*:')

    match = class_pattern.search(file_content)

    return match.group(1) if match else None


def modules(p: Path) -> tp.Iterator[Path]:
    for i in p.iterdir():
        if i.is_dir():
            continue
        if i.stem == 'base':
            continue
        if i.stem == '__init__':
            continue
        yield i


def main():
    p = Path('kubedantic/client/models')

    import_lines = []
    all_ = []

    for i in sorted(modules(p)):
        name = extract_class_name(i)
        import_lines.append(f'from .{i.stem} import {name}')
        all_.append(name)

    with open('kubedantic/client/models/__init__.py', 'w') as f:
        f.write('\n'.join(import_lines))
        f.write('\n\n\n')
        f.write('__all__ = [\n')

        for name in all_:
            f.write(f"    '{name}',\n")

        f.write(']')


if __name__ == "__main__":
    main()
