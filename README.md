API Data Collector
Description

API Data Collector is a modular Python project designed to consume and process REST APIs, with a strong focus on clean architecture, PEP 8 compliance, and modern Python development practices.

This project is intended as a learning-oriented implementation that demonstrates how to structure a real-world Python application, separate responsibilities, and write testable, maintainable code when working with external APIs.

Objectives

The main goals of this project are:

Apply a clean and modular project structure

Consume REST APIs using the requests library

Separate concerns between HTTP clients, business logic, and utilities

Practice modern Python tooling and workflows

Write unit tests for core business logic

Technologies Used

Python 3.13+

requests

uv

ruff

black

pytest

Project Structure
```text
api-data-collector/
├── src/
│   └── api_data_collector/
│       └── collector/
│           ├── main.py
│           ├── clients/
│           │   └── api_client.py
│           ├── config/
│           │   └── settings.py
│           ├── services/
│           │   └── data_service.py
│               ├── filters.py
│           ├── storage/
│           │   └── file_storage.py
│           └── utils/
│               ├── formatters.py
│               ├── logger.py
│               └── url_normalization.py
├── tests/
│   ├── clients/
│   ├── services/
│   └── utils/
├── pyproject.toml
├── README.md
└── .gitignore

```

How to Run

Install dependencies and set up the environment:

uv sync


Run development tools:

uv run ruff check .
uv run black .
uv run pytest

Architecture Overview

This project follows a clear separation of responsibilities, inspired by clean architecture principles.

ApiClient

The api_client module is responsible for all HTTP communication with external REST APIs.

The ApiClient class:

Is initialized with configuration values such as base URL and timeout

Uses the requests library to fetch data in JSON format

Exposes a get_json method that returns parsed JSON responses

Raises a RuntimeError when a request fails

This module isolates all networking concerns from the rest of the application.

DataService

The data_service module contains the business logic of the application.

The DataService class:

Depends on an ApiClient instance

Coordinates API calls

Processes raw API data into meaningful results

Delegates filtering logic to utility functions

For example, it can retrieve posts from an API and return a list of post titles that belong to a specific user.

Filters (Utilities)

Filtering logic is implemented as pure utility functions.

These functions:

Receive raw data structures (lists of dictionaries)

Apply domain-specific rules, such as filtering posts by user_id

Return simplified, human-readable results

If no data matches the filtering criteria, a ValueError is raised.

This design keeps the business logic testable and easy to extend.

URL Normalization Utilities

The project includes a utility module dedicated to URL normalization.

This module provides helper functions to:

Remove existing protocols (http://, https://)

Clean trailing slashes from URLs

Rebuild normalized URLs with a consistent protocol

Although this module is not yet integrated into the main execution flow, it represents a preparatory step for validating and sanitizing user-provided URLs before making HTTP requests.

Project Status

This project represents a foundational implementation focused on architecture, code quality, and testing.

It is intentionally scoped to demonstrate core concepts rather than feature completeness and serves as a reference project for junior developers learning how to build clean and maintainable Python applications.