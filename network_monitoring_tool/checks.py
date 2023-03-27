import subprocess

def ping_check(server):
    # Perform a ping check by running the 'ping' command in a subprocess
    command = ['ping', '-c', '1', server.hostname]
    process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return process.returncode == 0
