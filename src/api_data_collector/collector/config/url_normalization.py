def remove_prefix(url: str) -> str:
    """
    Removes http:// or https:// only from the start of the string."
    Returns the original string if no protocol is found
    """

    # 1. Clean the input
    url = url.strip().lower()

    # 2. Use 'removeprefix' method
    url = url.removeprefix("https://")
    url = url.removeprefix("http://")

    return url


def clean_end(url: str) -> str:
    """Clean the url end delete / at the end"""

    url = url.rstrip("/")

    return url


def add_protocol(url: str) -> str:
    "Add correct protocol"
    protocol = f"https://{url}"
    return protocol


def normalize_url(url: str) -> str:
    remove_prefix_apply = remove_prefix(url)
    clean_end_apply = clean_end(remove_prefix_apply)
    url_ready = add_protocol(clean_end_apply)

    return url_ready
