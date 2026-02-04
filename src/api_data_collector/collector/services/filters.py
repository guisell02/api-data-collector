def filter_posts_by_user(posts: list[dict], user_id: int) -> list[str]:
    """Filters post data and returns the titles belonging to a specific user.

    Args:
        posts (list[dict]): List of post objects retrieved from the API.
        user_id (int): Identifier of the user whose posts are requested.

    Returns:
        list[str]: Titles corresponding to the given user_id.

    Raises:
        ValueError: If no posts are found for the given user_id."""
    titles = []

    for post in posts:
        if post["userId"] == user_id:
            titles.append(post["title"])
    if not titles:
        raise ValueError(f"No posts found for this user {user_id}")
    return titles
