import subprocess

from kubedantic.client import create_from_content


def kustomize(__path_to_dir: str):
    result = subprocess.run(['kubectl', 'kustomize', __path_to_dir], capture_output=True, text=True)
    return list(map(create_from_content, result.stdout.split('---')))
