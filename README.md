# FastAPI Framework Template

This repository provides a basic framework for FastAPI projects, designed to help teams work with a unified structure inspired by Laravel's MVC architecture.

## Purpose
- Establish a consistent project structure for FastAPI development.
- Make collaboration easier for teams by following familiar patterns.
- Inspired by Laravel, with clear separation of controllers, models, and routes.

## Project Structure
- `app/http/controllers/` — Controllers (business logic)
- `app/models/` — Models (data structures / Pydantic schemas)
- `app/services/` — Services (business logic / ML)
- `routes/` — Route definitions
- `main.py` — FastAPI entry point
- `Dockerfile` & `docker-compose.yml` — Containerization setup

## Installation & Usage
1. **Clone this repository**
2. **Build and run with Docker:**
   ```sh
   docker compose build --no-cache
   docker compose up
   ```
3. Access the API at `http://localhost:8000/`
4. Interactive docs at `http://localhost:8000/docs`

---

## Naive Bayes - Spam Classifier

### What is it?
A **Gaussian Naive Bayes** implementation to classify emails as **spam** or **ham (not spam)** based on 5 email features.

### What does it compute?
- **Prior probabilities:** Probability of each class before observing the data (`P(spam)`, `P(ham)`)
- **Means:** The average value of each feature per class
- **Variances:** The spread of each feature per class
- **Posterior probabilities:** Using Bayes' theorem: `P(class|features) = P(features|class) * P(class) / P(features)`

### Features
| Feature | Description | Range |
|---------|------------|-------|
| `word_count` | Number of words in the email | >= 0 |
| `link_count` | Number of links | >= 0 |
| `has_urgent_words` | Contains urgent words | 0 or 1 |
| `capital_ratio` | Uppercase letter ratio | 0.0 - 1.0 |
| `special_char_count` | Special characters (!, $, etc.) | >= 0 |

### Endpoint
```
POST /naive-bayes
```

### Example - NOT spam email:
```sh
curl -X POST http://localhost:8000/naive-bayes \
  -H "Content-Type: application/json" \
  -d '{
    "word_count": 150,
    "link_count": 1,
    "has_urgent_words": 0,
    "capital_ratio": 0.05,
    "special_char_count": 2
  }'
```

### Example - SPAM email:
```sh
curl -X POST http://localhost:8000/naive-bayes \
  -H "Content-Type: application/json" \
  -d '{
    "word_count": 30,
    "link_count": 10,
    "has_urgent_words": 1,
    "capital_ratio": 0.50,
    "special_char_count": 20
  }'
```

### Expected response:
```json
{
  "prediction": 1,
  "label": "spam",
  "probabilities": {
    "ham": 0.0,
    "spam": 1.0
  },
  "model_params": {
    "class_prior": { "ham": 0.5, "spam": 0.5 },
    "class_count": { "ham": 12, "spam": 12 },
    "means_per_class": {
      "ham": { "word_count": 170.83, "link_count": 0.58, ... },
      "spam": { "word_count": 39.0, "link_count": 8.17, ... }
    },
    "variance_per_class": { ... }
  }
}
```

The `model_params` include all the **internal weights** of the model: priors, means and variances per class for each feature.

---

## License
This template is open-sourced software licensed under the [MIT license](https://opensource.org/licenses/MIT).
