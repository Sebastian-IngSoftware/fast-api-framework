from pydantic import BaseModel, Field


class NaiveBayesRequest(BaseModel):
    """
    Input model for Naive Bayes prediction.

    Represents the features of an email to classify it
    as spam or not spam (ham).
    """
    word_count: int = Field(
        ..., ge=0,
        description="Number of words in the email",
        examples=[150]
    )
    link_count: int = Field(
        ..., ge=0,
        description="Number of links in the email",
        examples=[2]
    )
    has_urgent_words: int = Field(
        ..., ge=0, le=1,
        description="Whether it contains urgent words (1 = yes, 0 = no)",
        examples=[0]
    )
    capital_ratio: float = Field(
        ..., ge=0.0, le=1.0,
        description="Uppercase letter ratio (0.0 to 1.0)",
        examples=[0.05]
    )
    special_char_count: int = Field(
        ..., ge=0,
        description="Number of special characters (!, $, etc.)",
        examples=[3]
    )


class NaiveBayesResponse(BaseModel):
    """Prediction response model."""
    prediction: int = Field(description="0 = ham, 1 = spam")
    label: str = Field(description="Human-readable label: 'spam' or 'ham (no spam)'")
    probabilities: dict = Field(description="Probabilities per class")
    model_params: dict = Field(description="Internal model parameters (weights, means, variances)")
