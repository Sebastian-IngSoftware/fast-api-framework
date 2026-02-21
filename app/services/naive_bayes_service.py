import numpy as np
from sklearn.naive_bayes import GaussianNB


class NaiveBayesService:
    """
    Naive Bayes service for email classification (spam / not spam).

    Features it receives:
    - word_count: Number of words in the email
    - link_count: Number of links in the email
    - has_urgent_words: Whether it contains urgent words (1 = yes, 0 = no)
    - capital_ratio: Uppercase letter ratio (0.0 to 1.0)
    - special_char_count: Number of special characters (!, $, etc.)

    Classes:
    - 0: Not spam (ham)
    - 1: Spam

    The model is trained with sample data upon initialization.
    """

    def __init__(self):
        self.model = GaussianNB()
        self._train()

    def _train(self):
        """Trains the model with sample data."""

        # Training data:
        # [word_count, link_count, has_urgent_words, capital_ratio, special_char_count]
        X_train = np.array([
            # No spam (ham)
            [150, 1, 0, 0.05, 2],
            [200, 0, 0, 0.03, 1],
            [80, 1, 0, 0.04, 0],
            [300, 2, 0, 0.06, 3],
            [120, 0, 0, 0.02, 1],
            [250, 1, 0, 0.04, 2],
            [180, 0, 0, 0.03, 0],
            [90, 1, 0, 0.05, 1],
            [160, 0, 0, 0.02, 2],
            [220, 1, 0, 0.04, 1],
            [170, 0, 0, 0.03, 0],
            [130, 1, 0, 0.06, 2],
            # Spam
            [50, 8, 1, 0.35, 15],
            [30, 10, 1, 0.50, 20],
            [20, 5, 1, 0.40, 12],
            [45, 7, 1, 0.30, 18],
            [60, 6, 1, 0.45, 10],
            [25, 9, 1, 0.55, 22],
            [35, 12, 1, 0.42, 16],
            [40, 8, 1, 0.38, 14],
            [55, 6, 1, 0.48, 19],
            [28, 11, 1, 0.52, 21],
            [42, 7, 1, 0.33, 13],
            [38, 9, 1, 0.41, 17],
        ])

        # Labels: 0 = not spam, 1 = spam
        y_train = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

        self.model.fit(X_train, y_train)

    def predict(self, features: dict) -> dict:
        """
        Makes a prediction given a set of features.

        Args:
            features: dict with word_count, link_count, has_urgent_words,
                      capital_ratio, special_char_count

        Returns:
            dict with the prediction, probabilities and model weights
        """
        X = np.array([[
            features["word_count"],
            features["link_count"],
            features["has_urgent_words"],
            features["capital_ratio"],
            features["special_char_count"],
        ]])

        prediction = self.model.predict(X)[0]
        probabilities = self.model.predict_proba(X)[0]

        return {
            "prediction": int(prediction),
            "label": "spam" if prediction == 1 else "ham (no spam)",
            "probabilities": {
                "ham": round(float(probabilities[0]), 4),
                "spam": round(float(probabilities[1]), 4),
            },
            "model_params": self._get_model_params(),
        }

    def _get_model_params(self) -> dict:
        """Returns the internal model parameters (weights, means, variances)."""
        feature_names = [
            "word_count",
            "link_count",
            "has_urgent_words",
            "capital_ratio",
            "special_char_count",
        ]

        return {
            "class_prior": {
                "ham": round(float(self.model.class_prior_[0]), 4),
                "spam": round(float(self.model.class_prior_[1]), 4),
            },
            "class_count": {
                "ham": int(self.model.class_count_[0]),
                "spam": int(self.model.class_count_[1]),
            },
            "means_per_class": {
                "ham": {
                    name: round(float(val), 4)
                    for name, val in zip(feature_names, self.model.theta_[0])
                },
                "spam": {
                    name: round(float(val), 4)
                    for name, val in zip(feature_names, self.model.theta_[1])
                },
            },
            "variance_per_class": {
                "ham": {
                    name: round(float(val), 4)
                    for name, val in zip(feature_names, self.model.var_[0])
                },
                "spam": {
                    name: round(float(val), 4)
                    for name, val in zip(feature_names, self.model.var_[1])
                },
            },
        }


# Global service instance (trained once)
naive_bayes_service = NaiveBayesService()
