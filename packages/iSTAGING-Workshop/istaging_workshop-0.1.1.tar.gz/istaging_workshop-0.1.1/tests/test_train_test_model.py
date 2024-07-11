import pytest
import pandas as pd
from iSTAGING_Workshop.train_test_model import model_train, model_test
import os

@pytest.fixture
def setup_data():
    """
    Fixture to set up test data and provide the path to the existing model file.

    Returns:
        tuple: Paths to the test data file and the model file.
    """
    # Define the path to the existing test data file
    data_path = os.path.join(os.path.dirname(__file__), 'test_data', 'pytest_test_data.csv')

    # Define the path to the existing model file
    model_path = os.path.join(os.path.dirname(__file__), 'test_data', 'pytest_model.pkl.gz')

    return data_path, model_path

def test_model_train(setup_data):
    """
    Test the model_train function.

    Args:
        setup_data (tuple): Paths to the test data file and the model file.
    """
    data_path, model_path = setup_data

    # Train the model using the test data
    results = model_train(data_path, model_path)

    # Check that the model training results are not empty
    assert results is not None

def test_model_test(setup_data):
    """
    Test the model_test function.

    Args:
        setup_data (tuple): Paths to the test data file and the model file.
    """
    data_path, model_path = setup_data

    # Test the model using the test data
    results = model_test(data_path, model_path)
    # Check that the length of the results matches the number of rows in the test data
    test_data = pd.read_csv(data_path)

    assert len(results['data']) == len(test_data)