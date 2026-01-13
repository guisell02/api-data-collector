import requests
from urllib.parse import urljoin


class ApiClient:
    """HTTP client for consuming REST APIs."""

    def __init__(self, base_url: str, timeout: int = 5) -> None:
        self.base_url = base_url
        self.timeout = timeout

    def get_json(self, endpoint: str) -> dict:
        """Perform a GET request to the given endpoint."""
        url = urljoin(self.base_url, endpoint)
        response = requests.get(url, timeout=self.timeout)

        if response.status_code != 200:
            raise RuntimeError(f"API error {response.status_code} while callign {url}")

        return response.json()
