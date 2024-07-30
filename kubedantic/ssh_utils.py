from typing_extensions import Self

import paramiko


def decode(encoded: bytes) -> str:
    try:
        result = encoded.decode('utf-8')
    except UnicodeDecodeError:
        try:
            result = encoded.decode('cp737')
        except UnicodeDecodeError:
            result = str(encoded)
    return result


class SshClientError(Exception):
    pass


class SshClient:
    def __init__(self, host: str, port: int, username: str, password: str) -> None:
        self.__host = host
        self.__port = port
        self.__username = username
        self.__password = password

    def __enter__(self) -> Self:
        self.__ssh = paramiko.SSHClient()
        self.__ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.__ssh.connect(self.__host, username=self.__username, password=self.__password, port=self.__port)
        self.__ssh.load_system_host_keys()
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        self.__ssh.close()

    def run_command(self, command: str, raise_error: bool) -> str:
        _stdin, stdout, stderr = self.__ssh.exec_command(command)
        result = decode(stdout.read()).strip()
        error = decode(stderr.read()).strip()
        if error and raise_error:
            raise SshClientError(error)
        elif error:
            result = f"{error}\n\n{result}"
        return result
