from sklearn.naive_bayes import GaussianNB
import numpy as np


class NaiveBayesModel:
    """
    Gaussian Naive Bayes model trained on a synthetic dataset.

    Features (per sample):
        - age          : customer age (years)
        - salary       : monthly salary (USD)
        - credit_score : credit score (300–850)

    Target classes:
        0 → "no_buy"
        1 → "buy"
    """

    CLASSES = {0: "no_buy", 1: "buy"}

    # Synthetic training data: [age, salary, credit_score]
    _X_TRAIN = np.array([
        [22,  1500, 320],
        [25,  2000, 400],
        [30,  3500, 500],
        [35,  5000, 620],
        [40,  7000, 700],
        [45,  8500, 750],
        [50, 10000, 780],
        [55, 12000, 800],
        [23,  1200, 310],
        [28,  1800, 380],
        [33,  4000, 530],
        [38,  6000, 660],
        [43,  9000, 730],
        [48, 11000, 760],
        [53, 13000, 810],
        [60, 15000, 840],
    ], dtype=float)

    _Y_TRAIN = np.array([
        0, 0, 0, 1, 1, 1, 1, 1,
        0, 0, 0, 1, 1, 1, 1, 1,
    ])

    # Train once at class definition time — shared across all instances
    _trained_model: GaussianNB = GaussianNB().fit(_X_TRAIN, _Y_TRAIN)

    def predict(self, age: int, salary: float, credit_score: int) -> dict:
        sample = np.array([[age, salary, credit_score]], dtype=float)
        label_index = int(self._trained_model.predict(sample)[0])
        probabilities = self._trained_model.predict_proba(sample)[0]
        return {
            "prediction": self.CLASSES[label_index],
            "probability_buy": round(float(probabilities[1]), 4),
            "probability_no_buy": round(float(probabilities[0]), 4),
        }
