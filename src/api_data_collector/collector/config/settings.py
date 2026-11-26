"""Configuration of the meteorological data collector for Pasto."""

# Open-Meteo Historical Weather API
API_BASE_URL = "https://archive-api.open-meteo.com"
API_ENDPOINT = "/v1/archive"

# Ubicación de referencia: Pasto, Nariño, Colombia.
LOCATION_NAME = "Pasto, Nariño, Colombia"
LATITUDE = 1.214578
LONGITUDE = -77.278117
TIMEZONE = "America/Bogota"

# Diez años calendario completos definidos en el alcance del proyecto.
START_DATE = "2016-01-01"
END_DATE = "2025-12-31"

# Variables diarias y modelo meteorológico.
MODEL = "era5"
DAILY_VARIABLES = (
    "temperature_2m_mean",
    "precipitation_sum",
)

# Configuraciones
REQUEST_TIMEOUT_SECONDS = 30
OUTPUT_DIRECTORY = "data"
DAILY_CSV_FILENAME = "pasto_daily_weather.csv"
MONTHLY_CSV_FILENAME = "pasto_monthly_weather_summary.csv"

CLIMATOLOGY_CSV_FILENAME = "pasto_monthly_climatology_2016_2025.csv"
