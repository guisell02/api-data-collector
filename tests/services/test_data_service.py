import pytest

from api_data_collector.collector.services.data_service import DataService


class FakeApiClient:
    def __init__(self, response):
        self.response = response
        self.endpoint = None
        self.params = None

    def get_json(self, endpoint, params=None):
        self.endpoint = endpoint
        self.params = params
        return self.response


def test_get_daily_weather_transforms_api_response():
    response = {
        "latitude": 1.25,
        "longitude": -77.25,
        "timezone": "America/Bogota",
        "daily_units": {
            "time": "iso8601",
            "temperature_2m_mean": "°C",
            "precipitation_sum": "mm",
        },
        "daily": {
            "time": ["2025-01-01"],
            "temperature_2m_mean": [15.2],
            "precipitation_sum": [3.4],
        },
    }
    client = FakeApiClient(response)
    service = DataService(client)

    result = service.get_daily_weather()

    assert result["records"] == [
        {
            "date": "2025-01-01",
            "temperature_2m_mean_c": 15.2,
            "precipitation_sum_mm": 3.4,
        }
    ]
    assert result["timezone"] == "America/Bogota"
    assert result["returned_coordinates"] == {
        "latitude": 1.25,
        "longitude": -77.25,
    }
    assert client.endpoint == "/v1/archive"
    assert client.params["timezone"] == "America/Bogota"


def test_get_daily_weather_rejects_response_without_daily_section():
    client = FakeApiClient({"timezone": "America/Bogota"})
    service = DataService(client)

    with pytest.raises(ValueError, match="daily"):
        service.get_daily_weather()


def test_get_daily_weather_rejects_series_with_different_lengths():
    response = {
        "daily": {
            "time": ["2025-01-01"],
            "temperature_2m_mean": [15.2],
            "precipitation_sum": [],
        }
    }
    service = DataService(FakeApiClient(response))

    with pytest.raises(ValueError, match="longitudes"):
        service.get_daily_weather()
