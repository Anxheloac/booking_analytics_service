# Booking & Analytics Platform API

A modern, scalable booking backend built with **FastAPI** and **SQLAlchemy Async**.  
Supports booking creation, analytics on booking data, and clean modular architecture.

---

## Features

- Async CRUD operations for bookings with SQLAlchemy AsyncSession  
- Analytics endpoints:  
  - Revenue by property  
  - Cancellation rate  
  - Bookings grouped by source  
- Custom error handling and validation with detailed API responses  
- Pydantic v2 models with field descriptions for OpenAPI docs  
- Middleware for rate limiting and IP whitelisting  
- Unit and integration tests using `pytest` and `pytest-asyncio`  

---

## Tech Stack

- Python 3.11+  
- FastAPI  
- Pydantic v2  
- SQLAlchemy Async ORM  
- PostgreSQL  
- pytest + pytest-asyncio

---

## Getting Started

### Prerequisites

- Python 3.11 or newer  
- PostgreSQL  
- [Docker](https://www.docker.com/) (optional, for containerized deployment)

### Installation

1. Clone this repo:

```bash
git clone https://github.com/anxhelo-akrobati/booking-analytics-api.git
cd booking-analytics-api

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Linux/macOS:
source venv/bin/activate

# On Windows (PowerShell):
venv\Scripts\Activate.ps1

# On Windows (cmd):
venv\Scripts\activate.bat

# Install dependencies
pip install -r requirements.txt

# Set environment variables (example for Linux/macOS)
export DATABASE_URL=postgresql+asyncpg://user:password@localhost/dbname

# Run database migrations (adjust if using Alembic or another tool)
alembic upgrade head

# Start the development server
uvicorn app.main:app --reload
```
Open your browser and go to:

Swagger UI (interactive API docs):
http://localhost:8000/docs

ReDoc (alternative API docs):
http://localhost:8000/redoc

![API Screenshot](docs/api_screenshot.png)