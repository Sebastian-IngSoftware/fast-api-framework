from app.models.naive_bayes import NaiveBayesRequest, NaiveBayesResponse
from app.services.naive_bayes_service import naive_bayes_service


class NaiveBayesController:
    @staticmethod
    def predict(request: NaiveBayesRequest) -> NaiveBayesResponse:
        """Receives email features and returns the prediction."""
        result = naive_bayes_service.predict(request.model_dump())
        return NaiveBayesResponse(**result)
