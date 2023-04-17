import subprocess
from .base import BaseChecker

class PingChecker(BaseChecker):
    """
    Checker class for ping checks.
    """
    @classmethod
    def check(cls, server):
        """
        Perform a ping check on the specified server and return the result.
        """
        result = subprocess.run(["ping", "-c", "1", server], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        online = result.returncode == 0
        return {"type": "ping", "server": server, "online": online}
