from unittest.mock import patch
import pytest
from api_data_collector.collector.clients.api_client import ApiClient


# - mockear requests.get
@patch("api_data_collector.collector.clients.api_client.requests.get")
def test_get_json_success(mock_get):

    # Mocks
    mock_get.return_value.json.return_value = {"key": ["Value"]}
    mock_get.return_value.status_code = 200

    # Execute the real function
    client = ApiClient("https://api.test")
    result = client.get_json("/posts")

    # Verify the result
    assert result == {"key": ["Value"]}

    # Verify behavior
    mock_get.assert_called_once_with("https://api.test/posts", timeout=5)


# Test2 verify status code


@patch("api_data_collector.collector.clients.api_client.requests.get")
def test_get_json_raises_error_on_bad_status(mock_get):
    # mockear status code expected
    mock_get.return_value.status_code = 400

    # Execute real function
    client = ApiClient("x")

    # Verify case error
    with pytest.raises(RuntimeError):
        client.get_json("/posts")
