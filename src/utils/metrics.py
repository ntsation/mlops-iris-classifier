from sklearn.metrics import accuracy_score

class Metrics:
    """Classe para avaliação de métricas."""
    @staticmethod
    def calculate_accuracy(y_true, y_pred) -> float:
        """Calcula a precisão."""
        return accuracy_score(y_true, y_pred)
