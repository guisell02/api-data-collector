# API Data Collector

## Description

Modular Python project designed to consume and process REST APIs, focused on clean project structure, PEP 8 compliance, and modern Python development workflows.  
The project serves as a learning-oriented implementation to apply best practices in API consumption, code quality, and testing.

---

## General Objective

Consolidate best practices in Python development, including:

- Project structuring and modular design
- API consumption using `requests`
- Use of modern tooling such as `uv`, `ruff`, `black`, and `pytest`

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


## How to Execute 

Install dependencies and set up the environment 

uv sync

Run development tools:

uv run ruff check .
uv run black .
uv run pytest


## Status project
Project in early development stage.
Currently includes the base structure and development tooling configuration.