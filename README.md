# Iris Classifier MLOps Project

This project is an example of how to apply MLOps for sorting Iris flowers using BentoML, MLflow, DVC, and scikit-learn. The model is trained, saved, and served using BentoML, with experiment tracking via MLflow and data versioning with DVC.

## Project Structure

The project structure is organized as follows:

```
mlops-iris-classifier/
├── services/
│ └── iris_service.py # BentoML Service to serve the trained model
├── date/
│ └── iris.csv # Iris Data (used for training)
├── models/
│ └── iris_classifier.pkl # Trained model (saved by MLflow and BentoML)
├── train.py # Script to train the model and register with MLflow and BentoML
├── requirements.txt # Project dependencies
└── README.md
```


- **`services/iris_service.py`**: Contains the BentoML service that loads the model and exposes an API to make predictions.
- **`train.py`**: Script that trains the classification model using Random Forest, records the results with MLflow, and saves the model with BentoML.
- **`data/iris.csv`**: Data used for training (CSV file).
- **`models/iris_classifier.pkl`**: File with the trained model, saved by BentoML and MLflow.
- **`requirements.txt`**: Contains all the dependencies necessary for the project to function.

## Requirements

Before running the project, make sure you have Python 3.12+ installed.

### Install dependencies

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```

2. Activate the virtual environment:
   - On Linux/MacOS:
     ```bash
     source .venv/bin/activate
     ```
   - On Windows:
     ```bash
     .venvScriptsactivate
     ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### DVC Configuration

This project uses DVC for data versioning. To configure DVC, run:

1. Initialize the DVC:
   ```bash
   Divine Init
   ```

2. Download the sample data:
   ```bash
   dvc pull
   ```


## How to Run

### 1. Model Training

To train the model, run the 'train.py' script. It will:
- Load the 'date/iris.csv' data.
- Train a Random Forest model.
- Register the model and its metrics with MLflow.
- Save the template using BentoML.

Run the script with the following command:

```bash
python train.py
```

### 2. Serving the Model with BentoML

Once you've trained and saved the model, you can serve the model's API using BentoML. The service will be available locally.

To run the BentoML service, run:

```bash
Bentoml serves services.iris_service
```

This will launch a server at the 'http://127.0.0.1:3000' URL where the API will be available.

### 3. Making Predictions

You can make predictions using an HTTP client (such as 'curl' or 'Postman'), sending an input array to the API. The input and output format will be a **NumpyNdarray**.

Example of how to make a request using curl:

```bash
curl -X 'POST' 
  'http://127.0.0.1:3000/classify' 
  -H 'accept: application/json' 
  -h 'content-type: application/json' 
  -d '[[5.1, 3.5, 1.4, 0.2]]'
```

This will send a trait vector to the API, which will return the model's prediction.

## Technologies Used

- **BentoML**: Framework for serving and managing machine learning models.
- **MLflow**: Model lifecycle management platform for tracking experiments and registering models.
- **DVC**: Data version control, for dataset management in the project.
- **scikit-learn**: Library for machine learning, used to train the classification model.
