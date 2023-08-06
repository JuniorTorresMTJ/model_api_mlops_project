import numpy as np
import pytest

""" 
>>>model_output = [-1, 1, -1, 1, 1, -1, 1] 
"""
model_output = [-1, 1, -1, 1, 1, -1, 1]


def check_model_output(model_output):
    unique_values = np.unique(model_output)

    for value in unique_values:
        assert value in [-1, 1], f'Invalid value {value} in model output'


def model_prediction_function():
    # Esta é apenas uma função fictícia para ilustrar. Na prática,
    # você deve chamar a função que obtém as previsões do seu modelo.
    return [-1, 1, -1, 1, 1, -1, 1]


def test_prediction_values():
    predictions = model_prediction_function()
    check_model_output(predictions)
