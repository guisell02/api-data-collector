# src/collector/main.py

from api_data_collector.collector.clients.api_client import ApiClient
from api_data_collector.collector.services.data_service import DataService
from api_data_collector.collector.config.settings import BASE_URL, DEFAULT_TIMEOUT


def main() -> None:
    api_client = ApiClient(
     BASE_URL, DEFAULT_TIMEOUT
    )

    service = DataService(api_client)

    user_id = 1
    titles = service.get_post_titles_by_user(user_id)

    print(f"Post titles for user {user_id}:")
    for title in titles:
        print(f"- {title}")


if __name__ == "__main__":
    main()
