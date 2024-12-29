import mlflow
import mlflow.sklearn
import bentoml

class ModelRegistry:
    """Classe para registrar modelos com MLflow e BentoML."""
    @staticmethod
    def log_model_mlflow(model, experiment_name, params, metrics):
        """Registra o modelo no MLflow."""
        mlflow.set_experiment(experiment_name)
        with mlflow.start_run():
            mlflow.log_params(params)
            mlflow.log_metrics(metrics)
            mlflow.sklearn.log_model(model, "model")

    @staticmethod
    def save_model_bentoml(model, model_name):
        """Salva o modelo no BentoML."""
        bentoml.sklearn.save_model(model_name, model)
