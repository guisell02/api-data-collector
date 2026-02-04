# API Data Collector

## Description

API Data Collector is a modular Python project designed to consume and process REST APIs,
with a strong focus on clean architecture, PEP 8 compliance, and modern Python development practices.

This project is intended as a learning-oriented implementation that demonstrates how to structure
a real-world Python application, separate responsibilities, and write testable, maintainable code
when working with external APIs.

---

## Objectives

The main goals of this project are:

- Apply clean and modular project structure
- Consume REST APIs using the `requests` library
- Separate concerns between HTTP clients, business logic, and utilities
- Practice modern Python tooling and workflows
- Write unit tests for core logic

---

## Technologies Used

- Python 3.13+
- requests
- uv
- ruff
- black
- pytest

---

## Project Structure

api-data-collector
├── src
│   └── collector
│       ├── __init__.py
│       ├── main.py
│       ├── config
│       │   └── settings.py
│       ├── clients
│       │   └── api_client.py
│       ├── services
│       │   └── data_service.py
│       ├── storage
│       │   └── file_storage.py
│       └── utils
│           ├── formatters.py
│           └── logger.py
├── tests
│   └── test_data_service.py
├── pyproject.toml
├── README.md
└── .gitignore



---

## How to Run

Install dependencies and set up the environment:

uv sync
Run development tools:

uv run ruff check .
uv run black .
uv run pytest
Architecture Overview
This project follows a clear separation of responsibilities.

ApiClient
The api_client module is responsible for all HTTP communication with external REST APIs.
It uses the requests library to fetch data in JSON format.

The ApiClient class:

Is initialized with configuration values such as base URL and timeout

Exposes a get_json method to retrieve parsed JSON data

Raises a RuntimeError when the request fails

DataService
The data_service module contains the business logic of the application.
It depends on an ApiClient instance to retrieve data, but it does not handle HTTP concerns directly.

The DataService:

Coordinates API calls

Processes raw data into meaningful results

Delegates filtering logic to utility functions

For example, it can retrieve posts from an API and return a list of post titles
that belong to a specific user.

Filters
Filtering logic is implemented as pure utility functions.
These functions receive raw data structures and apply domain-specific rules,
such as filtering posts by user_id.

If no data matches the filtering criteria, a ValueError is raised.

This separation ensures the codebase remains testable, maintainable, and easy to extend.

# Project Status
This project represents a foundational implementation focused on architecture,
code quality, and testing.

It is intentionally scoped to demonstrate core concepts rather than feature completeness.