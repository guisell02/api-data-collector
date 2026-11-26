from collections.abc import Mapping
from typing import Any
from urllib.parse import urljoin

import requests


class ApiClient:
    """Cliente HTTP para consumir API REST."""

    def __init__(self, base_url: str, timeout: int = 5) -> None:
        self.base_url = base_url
        self.timeout = timeout

    def get_json(
        self,
        endpoint: str,
        params: Mapping[str, str | int | float] | None = None,
    ) -> Any:
        """Envía una solicitud GET y devuelve la respuesta en formato JSON.

        Args:
            endpoint: Ruta de la API, por ejemplo ``/v1/archive``.
            params: Parámetros opcionales que se envían en la URL.
        """
        base_url = f"{self.base_url.rstrip('/')}/"
        endpoint = endpoint.lstrip("/")
        url = urljoin(base_url, endpoint)

        try:
            if params is None:
                response = requests.get(url, timeout=self.timeout)
            else:
                response = requests.get(
                    url,
                    params=params,
                    timeout=self.timeout,
                )
        except requests.exceptions.RequestException as error:
            raise RuntimeError(
                f"No se pudo conectar con la API en {url}: {error}"
            ) from error

        if not 200 <= response.status_code < 300:
            raise RuntimeError(
                f"La API respondió con el estado HTTP "
                f"{response.status_code} al consultar {url}"
            )

        try:
            return response.json()
        except ValueError as error:
            raise RuntimeError(
                f"La respuesta de {url} no contiene JSON válido."
            ) from error
