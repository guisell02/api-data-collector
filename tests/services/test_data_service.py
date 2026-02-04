import pytest
from api_data_collector.collector.services.data_service import DataService


class FakeApiClient:
    def get_json(self, endpoint: str):
        return [
            {"userId": 1, "title": "Hello"},
            {"userId": 2, "title": "World"},
            {"userId": 1, "title": "Python"},
        ]


def test_get_post_titles_by_user_returns_titles():
    """Returns the post titles that correspond to the given user_id."""
    fake_client = FakeApiClient()
    service = DataService(fake_client)

    result = service.get_post_titles_by_user(user_id=1)

    assert result == ["Hello", "Python"]


def test_get_post_titles_by_user_raises_error_when_user_not_found():
    """Raises ValueError when no posts are found for the given user."""
    service = DataService(FakeApiClient())

    with pytest.raises(ValueError):
        service.get_post_titles_by_user(user_id=99)
