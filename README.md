# FastAPI Framework Template

This repository provides a basic framework for FastAPI projects, designed to help teams work with a unified structure inspired by Laravel's MVC architecture.

## Purpose
- Establish a consistent project structure for FastAPI development.
- Make collaboration easier for teams by following familiar patterns.
- Inspired by Laravel, with clear separation of controllers, models, and routes.

## Project Structure
- `app/http/controllers/` — Controllers (business logic)
- `app/models/` — Models (data structures)
- `routes/` — Route definitions
- `main.py` — FastAPI entry point
- `Dockerfile` & `docker-compose.yml` — Containerization setup

## Installation & Usage
1. **Clone this repository**
2. **Build and run with Docker:**
   ```sh
   docker compose up --build
   ```
3. Access the API at `http://localhost:8000/`

## License
This template is open-sourced software licensed under the [MIT license](https://opensource.org/licenses/MIT).
