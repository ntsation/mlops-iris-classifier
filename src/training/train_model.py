from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from src.utils.metrics import Metrics

class ModelTrainer:
    """Classe responsável pelo treinamento do modelo."""
    def __init__(self, model=None):
        self.model = model or RandomForestClassifier(n_estimators=100, random_state=42)

    def train(self, X, y):
        """Treina o modelo."""
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)
        y_pred = self.model.predict(X_test)
        accuracy = Metrics.calculate_accuracy(y_test, y_pred)
        return self.model, accuracy
