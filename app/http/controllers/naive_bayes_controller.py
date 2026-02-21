from app.models.naive_bayes_model import NaiveBayesModel
from app.schemas.naive_bayes_schema import NaiveBayesInput, NaiveBayesPrediction

_model = NaiveBayesModel()


class NaiveBayesController:
    @staticmethod
    def predict(data: NaiveBayesInput) -> NaiveBayesPrediction:
        result = _model.predict(
            age=data.age,
            salary=data.salary,
            credit_score=data.credit_score,
        )
        return NaiveBayesPrediction(**result)
