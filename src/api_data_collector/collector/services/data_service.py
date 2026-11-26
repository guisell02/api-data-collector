from collections.abc import Mapping
from typing import Any

from api_data_collector.collector.clients.api_client import ApiClient
from api_data_collector.collector.config.settings import (
    API_ENDPOINT,
    DAILY_VARIABLES,
    END_DATE,
    LATITUDE,
    LONGITUDE,
    MODEL,
    START_DATE,
    TIMEZONE,
)


class DataService:
    """Contiene las operaciones para obtener y preparar datos."""

    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client

    def get_daily_weather(self) -> dict[str, Any]:
        """Consulta Open-Meteo y organiza sus datos diarios."""
        params = {
            "latitude": LATITUDE,
            "longitude": LONGITUDE,
            "start_date": START_DATE,
            "end_date": END_DATE,
            "daily": ",".join(DAILY_VARIABLES),
            "timezone": TIMEZONE,
            "models": MODEL,
        }

        response = self.api_client.get_json(API_ENDPOINT, params=params)

        if not isinstance(response, Mapping):
            raise ValueError("La respuesta de la API no es un objeto JSON.")

        daily_data = response.get("daily")
        if not isinstance(daily_data, Mapping):
            raise ValueError("La respuesta no contiene la sección 'daily'.")

        dates = daily_data.get("time")
        temperatures = daily_data.get("temperature_2m_mean")
        precipitation = daily_data.get("precipitation_sum")

        if not all(
            isinstance(series, list) for series in (dates, temperatures, precipitation)
        ):
            raise ValueError(
                "La API no devolvió las fechas y variables diarias esperadas."
            )

        if not (len(dates) == len(temperatures) == len(precipitation)):
            raise ValueError(
                "Las series de fechas, temperatura y precipitación "
                "tienen longitudes distintas."
            )

        records = [
            {
                "date": observed_date,
                "temperature_2m_mean_c": temperature,
                "precipitation_sum_mm": rain,
            }
            for observed_date, temperature, rain in zip(
                dates,
                temperatures,
                precipitation,
                strict=True,
            )
        ]

        return {
            "records": records,
            "requested_coordinates": {
                "latitude": LATITUDE,
                "longitude": LONGITUDE,
            },
            "returned_coordinates": {
                "latitude": response.get("latitude"),
                "longitude": response.get("longitude"),
            },
            "timezone": response.get("timezone"),
            "daily_units": response.get("daily_units", {}),
        }
