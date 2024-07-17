import pytest
# TODO: add necessary import
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder, LabelBinarizer
from ml.data import apply_label
from ml.model import (
    compute_model_metrics,
    inference,
    load_model,
    performance_on_categorical_slice,
    save_model,
    train_model,
)
# TODO: implement the first test. Change the function name and input as needed
def test_apply_labels():
    """
    Test converting binary label to string output.
    """
    # Test case: label is 1
    inference = [1]
    result = apply_label(inference)
    assert result == ">50K", f"Expected '>50K' but got {result}"

    # Test case: label is 0
    inference = [0]
    result = apply_label(inference)
    assert result == "<=50K", f"Expected '<=50K' but got {result}"

    # Test case: invalid label (should not happen in practice, but good to test)
    inference = [2]
    result = apply_label(inference)
    assert result is None, f"Expected None for invalid input but got {result}"


# TODO: implement the second test. Change the function name and input as needed
def test_train_model ():
    """
    Test training a RandomForest model on a simple dataset.
    """
    # Your code here
    X_train = np.array([[1,2],[3,4],[5,6],[7,8]])
    y_train = np.array([0,1,2,3])
    model=train_model(X_train,y_train)
    assert isinstance(model, RandomForestClassifier), "Model is not a RandomForestClassifier"
    assert model.n_estimators > 0, "Model does not have estimators"
    


# TODO: implement the third test. Change the function name and input as needed
def test_compute_model_metrics ():
    """
    Test computing precision, recall, and fbeta score.
    """
    # Your code here
    y = np.array([0,1,0,1])
    preds = np.array([0,1,0,0])
    precision, recall, fbeta = compute_model_metrics(y,preds)
    assert precision == 1.0, "Precision calculation is incorrect"
    assert recall == 0.5, "Recall calculation is incorrect"
    assert fbeta == 0.6666666666666666, "Fbeta calculation is incorrect"
