import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import mlflow
import mlflow.sklearn
import bentoml
import dvc.api

# Configurar o DVC para carregar os dados
data_url = dvc.api.get_url('data/iris.csv')
df = pd.read_csv(data_url)

# Preparar os dados
X = df.drop('target', axis=1)
y = df['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Configurar o MLflow
mlflow.set_experiment("iris_classification")

with mlflow.start_run():
    # Treinar o modelo
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Avaliar o modelo
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    # Registrar métricas e parâmetros no MLflow
    mlflow.log_param("n_estimators", 100)
    mlflow.log_metric("accuracy", accuracy)
    
    # Salvar o modelo com MLflow
    mlflow.sklearn.log_model(model, "model")
    
    # Salvar o modelo com BentoML
    bentoml.sklearn.save_model("iris_classifier", model)

print(f"Modelo treinado e salvo. Acurácia: {accuracy}")