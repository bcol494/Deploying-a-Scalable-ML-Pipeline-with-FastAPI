import pytest
# TODO: add necessary import
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from ml.model import train_model, compute_model_metrics, inference

# TODO: implement the first test. Change the function name and input as needed
def test_train_model():
    """
    # Test that train_model returns a trained RandomForestClassifier.
    """
    # Your code here
    X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
    y = np.array([0, 0, 1, 1])
    model = train_model(X, y)
    assert isinstance(model, RandomForestClassifier)


# TODO: implement the second test. Change the function name and input as needed
def test_inference():
    """
    # Test that inference returns predictions of the correct length and type.
    """
    # Your code here
    X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
    y = np.array([0, 0, 1, 1])
    model = train_model(X, y)
    preds = inference(model, X)
    assert len(preds) == len(y)
    assert isinstance(preds, np.ndarray)


# TODO: implement the third test. Change the function name and input as needed
def test_compute_model_metrics():
    """
    # Test that metrics calculation returns valid floats between 0 and 1.
    """
    # Your code here
    y = np.array([1, 0, 1, 1, 0])
    preds = np.array([1, 0, 1, 0, 0])
    precision, recall, f1 = compute_model_metrics(y, preds)

    assert isinstance(precision, float)
    assert isinstance(recall, float)
    assert isinstance(f1, float)
    assert 0 <= precision <= 1
    assert 0 <= recall <= 1
    assert 0 <= f1 <= 1
