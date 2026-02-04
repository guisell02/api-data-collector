"First test: Remove prefix"

from api_data_collector.collector.utils.url_normalization import (
    remove_prefix,
    clean_end,
    add_protocol,
    normalize_url,
)


def test_force_clean_start_url():
    input_url = "https://jsonplaceholder.typicode.com"
    expected = "jsonplaceholder.typicode.com"

    assert remove_prefix(input_url) == expected


def test_force_clean_end_url():
    input_url = "https://jsonplaceholder.typicode.com/"
    expected = "https://jsonplaceholder.typicode.com"

    assert clean_end(input_url) == expected


def test_force_apply_correct_protocol():
    input_url = "jsonplaceholder.typicode.com"
    expected = "https://jsonplaceholder.typicode.com"

    assert add_protocol(input_url) == expected


def test_normalize_url():
    input_url = "https://jsonplaceholder.typicode.com/"
    expected = "https://jsonplaceholder.typicode.com"

    assert normalize_url(input_url) == expected
