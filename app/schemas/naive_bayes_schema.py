from pydantic import BaseModel, Field


class NaiveBayesInput(BaseModel):
    age: int = Field(..., ge=18, le=100, description="Age of the customer")
    salary: float = Field(..., ge=0, description="Monthly salary in USD")
    credit_score: int = Field(..., ge=300, le=850, description="Credit score (300–850)")


class NaiveBayesPrediction(BaseModel):
    prediction: str = Field(..., description="Predicted class: 'buy' or 'no_buy'")
    probability_buy: float = Field(..., description="Probability of buying")
    probability_no_buy: float = Field(..., description="Probability of not buying")
