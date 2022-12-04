import paramiko
import subprocess
import pytest
import re
import shlex

host = '127.0.0.1'
port = '5679'
password = '123'
username = 'pc1'


@pytest.fixture(scope='function')
def server():
    client = paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, port=port, username=username, password=password)
    client.exec_command("iperf -s -P 1 > /dev/null 2>&1 &")
    client.close()


@pytest.fixture(scope='function')
def client(server):
    command = f"iperf -c {host} -i 1"
    args = shlex.split(command)
    res = subprocess.check_output(args).decode(encoding="UTF-8")
    if re.match(r"^-*\nClient\sconnecting\sto", res):
        return res, None
    else:
        return None, res