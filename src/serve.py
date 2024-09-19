import bentoml
import numpy as np
from bentoml.io import NumpyNdarray

iris_clf_runner = bentoml.sklearn.get("iris_classifier:latest").to_runner()

svc = bentoml.Service("iris_classifier", runners=[iris_clf_runner])

@svc.api(input=NumpyNdarray(), output=NumpyNdarray())
def classify(input_series: np.ndarray) -> np.ndarray:
    # Check if input is 1D and reshape if necessary
    if input_series.ndim == 1:
        input_series = input_series.reshape(1, -1)
    
    result = iris_clf_runner.predict.run(input_series)
    return result
