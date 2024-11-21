# FastAPI CRUD 

## Overview
i
This project is a FastAPI-based application designed in a repository patter to explore the FastAPI capabilities.

---

## Features

- **FastAPI**: High-performance API framework with `OpenAPI` documentation.
- **SQLAlchemy**: ORM based database interaction.
- **Alembic**: Database migrations.
- **Pydantic**: Data validation
- **Environment Configuration**: Managed with `python-dotenv`.
- **Testing**: Comprehensive unit and integration tests using `pytest` and `httpx`.
- **Pre-Commit Hooks**: Enforces coding standards and formatting using hooks to validation libraries.
- **Integrated Server** Through the python library`uvicorn`.

---

## Installation

### Prerequisites

- Python 3.10+
- PostgreSQL (optional, recommended)
- `pip` (Python package manager)

### Steps

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>```
2. Create a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # For Linux/macOS
   .venv\Scripts\activate     # For Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure environment variables:
   - Create a .env file based on the .env.example provided in the repository.

6. Apply database migrations:
   ```bash
   alembic upgrade head
   ```
7. Run the application:
   ```bash
   uvicorn main:app
   ```
## Usage
1. Access the API documentation at http://localhost:8000/docs.
2. Test endpoints interactively using Swagger UI or ReDoc.

![image](https://github.com/user-attachments/assets/1865da33-e2a2-4632-b119-4a4799206228)

## Pre-commit Hooks 
git configuration file to ensure code quality and formatting before committing
```bash
pre-commit install
pre-commit run --all-files
```

## Running tests
Run the unit and integration tests just using:
```bash
pytest
```




