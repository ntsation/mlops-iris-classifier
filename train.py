from src.data.data_loader import DataLoader
from src.training.train_model import ModelTrainer
from src.registry.model_registry import ModelRegistry
from config.config import Config

def main():
    # Carregamento de dados
    loader = DataLoader(Config.DATA_PATH)
    df = loader.load_data()
    X = df.drop('target', axis=1)
    y = df['target']

    # Treinamento do modelo
    trainer = ModelTrainer()
    model, accuracy = trainer.train(X, y)

    # Registro do modelo
    ModelRegistry.log_model_mlflow(
        model, 
        Config.EXPERIMENT_NAME, 
        params={"n_estimators": Config.N_ESTIMATORS}, 
        metrics={"accuracy": accuracy}
    )
    ModelRegistry.save_model_bentoml(model, Config.MODEL_NAME)

    print(f"Model trained and saved. Accuracy: {accuracy}")

if __name__ == "__main__":
    main()
