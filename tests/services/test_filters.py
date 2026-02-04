import pytest
from api_data_collector.collector.services.filters import filter_posts_by_user


def test_filter_posts_by_user_returns_titles():
    """Returns all post titles that belong to the specified user."""
    posts = [
        {"userId": 1, "title": "Hello"},
        {"userId": 2, "title": "World"},
        {"userId": 1, "title": "Python"},
    ]

    result = filter_posts_by_user(posts, user_id=1)

    assert result == ["Hello", "Python"]


def test_filter_posts_by_user():
    """Raises ValueError when no posts match the given user_id."""
    posts = [{"userId": 1, "title": "Hello"}, {"userId": 1, "title": "Hello"}]

    with pytest.raises(ValueError):
        filter_posts_by_user(posts, user_id=5)
