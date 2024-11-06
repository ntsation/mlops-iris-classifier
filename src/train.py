import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import mlflow
import mlflow.sklearn
import bentoml
import dvc.api

# Configure DVC to load data
data_url = dvc.api.get_url('data/iris.csv')
df = pd.read_csv(data_url)

# Prepare the data
X = df.drop('target', axis=1)
y = df['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Configure MLflow
mlflow.set_experiment("iris_classification")

with mlflow.start_run():
    # Train the model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate the model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    # Register metrics and parameters in MLflow
    mlflow.log_param("n_estimators", 100)
    mlflow.log_metric("accuracy", accuracy)
    
    # Save the model with MLflow
    mlflow.sklearn.log_model(model, "model")
    
    # Save the model with BentoML
    bentoml.sklearn.save_model("iris_classifier", model)

print(f"Model trained and saved. Accuracy {accuracy}")