from typing_extensions import Self

import paramiko


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

    def run_command(self, command: str) -> str:
        _stdin, stdout, stderr = self.__ssh.exec_command(command)
        result = stdout.read().decode('utf-8').strip()
        error = stderr.read().decode('utf-8').strip()
        if error:
            raise SshClientError(error)
        return result
