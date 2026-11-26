from unittest.mock import patch

import pytest

from api_data_collector.collector.clients.api_client import ApiClient


@patch("api_data_collector.collector.clients.api_client.requests.get")
def test_get_json_sends_open_meteo_request_and_returns_json(mock_get):
    response_data = {
        "latitude": 1.25,
        "longitude": -77.25,
        "timezone": "America/Bogota",
    }
    request_params = {
        "latitude": 1.214578,
        "longitude": -77.278117,
        "start_date": "2016-01-01",
        "end_date": "2025-12-31",
        "daily": "temperature_2m_mean,precipitation_sum",
        "timezone": "America/Bogota",
        "models": "era5",
    }

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = response_data

    client = ApiClient(
        base_url="https://archive-api.open-meteo.com",
        timeout=30,
    )

    result = client.get_json("/v1/archive", params=request_params)

    assert result == response_data
    mock_get.assert_called_once_with(
        "https://archive-api.open-meteo.com/v1/archive",
        params=request_params,
        timeout=30,
    )


@patch("api_data_collector.collector.clients.api_client.requests.get")
def test_get_json_raises_error_when_api_returns_non_success_status(mock_get):
    mock_get.return_value.status_code = 400

    client = ApiClient(
        base_url="https://archive-api.open-meteo.com",
        timeout=30,
    )

    with pytest.raises(RuntimeError, match="400"):
        client.get_json("/v1/archive")
