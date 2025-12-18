from api_data_collector.collector.clients.api_client import ApiClient


def test_get_success():
    client = ApiClient("https://jsonplaceholder.typicode.com")
    response = client.get("/posts/1")
    assert response.status_code == 200
