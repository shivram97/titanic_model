

import pandas as pd
import  numpy as np
from sklearn.metrics import accuracy_score, classification_report
def evaluate_classification(y_pred,y_test):
    """
    Evaluate the performance of a classification model.

    Args:
        y_pred (array-like): Predicted labels.
        y_test (array-like): True labels.

    Returns:
        dict: A dictionary containing the following metrics:
            - accuracy (float): The accuracy score of the model.
            - classification_report (str): A detailed classification report.

    """
    res={}
    res["accuracy"] = accuracy_score(y_pred,y_test)
    res["classification_report"] = classification_report(y_pred,y_test)
    return res