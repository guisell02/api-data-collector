import requests


class ApiClient:
    """HTTP client for consuming REST APIs."""

    def __init__(self, base_url: str, timeout: int = 5) -> None:
        self.base_url = base_url
        self.timeout = timeout

    def get(self, endpoint: str) -> requests.Response:
        """Perform a GET request to the given endpoint."""
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, timeout=self.timeout)
        return response
