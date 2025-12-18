from api_data_collector.collector.clients.api_client import ApiClient


def main() -> None:
    client = ApiClient("https://jsonplaceholder.typicode.com")
    response = client.get("/posts/1")
    print(response.status_code)
    print(response.json())


if __name__ == "__main__":
    main()
