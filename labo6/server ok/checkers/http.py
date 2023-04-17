import requests
from .base import BaseChecker

class HTTPChecker(BaseChecker):
    def __init__(self, name, url):
        super().__init__(name)
        self.url = url

    def check(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                return True, "HTTP check succeeded"
            else:
                return False, f"HTTP check failed with status code {response.status_code}"
        except requests.exceptions.RequestException as e:
            return False, f"HTTP check failed with exception: {str(e)}"
