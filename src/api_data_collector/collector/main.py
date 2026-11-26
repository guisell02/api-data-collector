from pathlib import Path

from api_data_collector.collector.clients.api_client import ApiClient
from api_data_collector.collector.config.settings import (
    API_BASE_URL,
    DAILY_CSV_FILENAME,
    LOCATION_NAME,
    MONTHLY_CSV_FILENAME,
    OUTPUT_DIRECTORY,
    REQUEST_TIMEOUT_SECONDS,
    CLIMATOLOGY_CSV_FILENAME,
)
from api_data_collector.collector.services.aggregation import (
    build_monthly_summary,
    build_monthly_climatology,
)
from api_data_collector.collector.services.data_service import DataService
from api_data_collector.collector.storage.file_storage import save_csv


def main() -> None:
    api_client = ApiClient(
        base_url=API_BASE_URL,
        timeout=REQUEST_TIMEOUT_SECONDS,
    )
    service = DataService(api_client)

    weather_data = service.get_daily_weather()
    daily_records = weather_data["records"]

    if not daily_records:
        raise ValueError("La API no devolvió registros diarios.")

    monthly_records = build_monthly_summary(daily_records)
    climatology_records = build_monthly_climatology(monthly_records)
    output_directory = Path(OUTPUT_DIRECTORY)

    daily_path = save_csv(
        daily_records,
        output_directory / DAILY_CSV_FILENAME,
    )
    monthly_path = save_csv(
        monthly_records,
        output_directory / MONTHLY_CSV_FILENAME,
    )
    climatology_path = save_csv(
        climatology_records,
        output_directory / CLIMATOLOGY_CSV_FILENAME,
    )

    print(f"Datos meteorológicos de {LOCATION_NAME}")
    print(f"Zona horaria: {weather_data['timezone']}")
    print(f"Coordenadas solicitadas: {weather_data['requested_coordinates']}")
    print(f"Coordenadas reportadas por la API: {weather_data['returned_coordinates']}")
    print(f"Registros diarios: {len(daily_records)}")
    print(f"Resúmenes año-mes: {len(monthly_records)}")
    print(f"CSV diario: {daily_path}")
    print(f"CSV mensual: {monthly_path}")
    print(f"Promedios mensuales: {len(climatology_records)}")
    print(f"CSV de promedios mensuales: {climatology_path}")


if __name__ == "__main__":
    main()
