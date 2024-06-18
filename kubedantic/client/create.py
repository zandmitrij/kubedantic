import tempfile

import yaml

from .configmap import ConfigMap
from .job import Job
from .secret import Secret


def create_from_yaml(file: str):
    with open(file, 'r') as f:
        res = yaml.safe_load(f)
    kind = res['kind']
    if kind == 'ConfigMap':
        return ConfigMap.from_file(file)
    elif kind == 'Job':
        return Job.from_file(file)
    elif kind == 'Secret':
        return Secret.from_file(file)
    raise ValueError(f'kind {kind} unsupported')


def create_from_content(content: str):
    with tempfile.NamedTemporaryFile(prefix='temp_', suffix='.yml', dir='/tmp', mode='w+t') as temp_file:
        temp_file.write(content)
        temp_file.seek(0)
        return create_from_yaml(temp_file.name)
