import requests
from typing import Dict, Any, Optional, List

class TKTestDriver:
    def __init__(self, host: str, port: int, api_key: Optional[str] = None):
        self.base_url = f"http://{host}:{port}"
        self.api_key = api_key
        self.headers = {"X-API-Key": self.api_key} if self.api_key else {}

    def _send_request(self, method: str, endpoint: str, data: Optional[Dict] = None) -> Dict:
        url = f"{self.base_url}{endpoint}"
        response = requests.request(method, url, json=data, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def startup(self) -> Dict:
        return self._send_request("POST", "/startup")

    def shutdown(self) -> Dict:
        return self._send_request("POST", "/shutdown")

    def status(self) -> Dict:
        return self._send_request("GET", "/status")

    def wait_for_initialization(self) -> Dict:
        return self._send_request("GET", "/wait_for_initialization")

    def interact(self, method: str, args: List[Any] = []) -> Dict:
        data = {"method": method, "args": args}
        return self._send_request("POST", "/interact", data)
