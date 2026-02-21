# FastAPI Framework Template

This repository provides a basic framework for FastAPI projects, designed to help teams work with a unified structure inspired by Laravel's MVC architecture.

## Purpose
- Establish a consistent project structure for FastAPI development.
- Make collaboration easier for teams by following familiar patterns.
- Inspired by Laravel, with clear separation of controllers, models, and routes.

## Project Structure
- `app/http/controllers/` — Controllers (business logic)
- `app/models/` — Models (data structures and ML models)
- `app/schemas/` — Pydantic request/response schemas
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

---

## Naive Bayes — Purchase Prediction (`POST /naive-bayes`)

This endpoint uses a **Gaussian Naive Bayes** classifier to predict whether a customer is likely to make a purchase based on three features.

### What does the model calculate?
The model was trained on a synthetic dataset. Given a customer's **age**, **monthly salary**, and **credit score**, it returns:
- `prediction` — `"buy"` or `"no_buy"`
- `probability_buy` — probability (0–1) that the customer will buy
- `probability_no_buy` — probability (0–1) that the customer will not buy

### Request body (JSON)

| Field          | Type    | Required | Range       | Description                     |
|----------------|---------|----------|-------------|---------------------------------|
| `age`          | integer | ✅       | 18–100      | Customer age in years           |
| `salary`       | float   | ✅       | ≥ 0         | Monthly salary in USD           |
| `credit_score` | integer | ✅       | 300–850     | Credit score                    |

### Example — using `curl` inside Docker

```sh
curl -X POST "http://localhost:8000/naive-bayes" \
     -H "Content-Type: application/json" \
     -d '{"age": 35, "salary": 5000, "credit_score": 620}'
```

### Example response

```json
{
  "prediction": "buy",
  "probability_buy": 0.9312,
  "probability_no_buy": 0.0688
}
```

### Interactive docs
Once the container is running, open your browser at:
```
http://localhost:8000/docs
```
Navigate to **POST /naive-bayes** and use the **Try it out** button to send requests directly from the browser.

## License
This template is open-sourced software licensed under the [MIT license](https://opensource.org/licenses/MIT).
