# MLOps Project with Iris Classifier

This project demonstrates a complete MLOps pipeline using an iris classifier as an example. It integrates various modern MLOps tools and practices, including data versioning, experiment tracking, model packaging, and continuous deployment.

## Technologies Used

- **Python**: Primary programming language
- **scikit-learn**: For the classification model
- **MLflow**: For experiment tracking and model registry
- **BentoML**: For model packaging and serving
- **DVC (Data Version Control)**: For data versioning
- **GitHub Actions**: For CI/CD

## Project Structure

```
.
├── .github
│   └── workflows
│       └── mlops_pipeline.yml
├── data
│   └── iris.csv
├── models
│   └── model.pkl
├── src
│   ├── train.py
│   └── serve.py
├── .dvc
├── .gitignore
├── bentofile.yaml
├── requirements.txt
└── README.md
```

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/ntsation/project-mlops.git
   cd project-mlops
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up DVC:
   ```
   dvc init
   dvc add data/iris.csv
   ```

   For local usage:
   ```
   dvc remote add -d localremote /path/to/local/storage
   ```

   For Google Drive (recommended for CI/CD):
   ```
   dvc remote add -d myremote gdrive://your-drive-id
   ```

   After setting up the remote:
   ```
   dvc push
   ```

## Usage

### Training the Model

To train the model:

```
python src/train.py
```

This will train the model, log metrics with MLflow, and save the model using BentoML.

### Serving the Model

To serve the model locally:

```
bentoml serve src/serve.py:svc
```

### Building the BentoML Bundle

To build a BentoML bundle:

```
bentoml build
```

## CI/CD Pipeline

The file `.github/workflows/mlops_pipeline.yml` defines a CI/CD pipeline that is triggered on pushes to the main branch.

**Important Note on DVC and CI/CD:**
If you're using DVC with local storage, the CI/CD pipeline on GitHub Actions will fail when trying to access the data in DVC. This is because local storage is not accessible in the remote CI/CD environment.

To address this issue, you have a few options:

1. Use a remote DVC storage solution like Google Drive, AWS S3, or similar. This will allow the CI/CD pipeline to access the data.
   
2. If you must use local storage, consider adding the data to the Git repository for CI/CD purposes. You can create a separate branch for CI/CD that includes the data.

3. Modify the CI/CD pipeline to skip the DVC pull step when using local storage.

For local execution, using local DVC storage will work without issues.

The pipeline includes:

- Dependency installation
- DVC setup and pulling the data (may fail with local storage)
- Model training
- BentoML bundle build
- Tests (simulated)
- Deployment (simulated)

## Local Execution vs. CI/CD

- **Local Execution**: All steps, including DVC with local storage, will function as expected.
- **CI/CD**: If using DVC with local storage, the data pull step will fail. Consider the options mentioned above to resolve this.

## Monitoring and Iteration

Use the MLflow UI to visualize metrics and parameters:

```
mlflow ui
```