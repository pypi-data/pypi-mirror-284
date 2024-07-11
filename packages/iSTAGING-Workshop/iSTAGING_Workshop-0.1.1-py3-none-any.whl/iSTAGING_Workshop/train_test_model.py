import pandas as pd
import spare_scores as sp

def model_train(data_path_train, output_model_path):
    """
    Train a SPARE model using the specified training data and save the model to the specified path.

    Args:
        data_path_train (str): Path to the CSV file containing the training data.
        output_model_path (str): Path to save the trained model.

    Returns:
        dict: Results of the training process.
    """
    # Load the training data, define the target variable to predict, 
    # and specify the type of predictor to use (Support Vector Machine).
    data = pd.read_csv(data_path_train)
    to_predict = "Sex"
    predictor_type = "SVM"

    # Define the positive group for classification and key variable
    positive_group = "M"
    key_variable = "ID"

    # Define the variables to be used for training - ICV, TOTALBRAIN, CSF, GM, WM ROIs.
    train_variables = ["702", "701", "600", "601", "604"]

    # Identify variables to ignore during training - rest, and kernel type for the SVM
    ignore_variables = list(set(data.columns) - set(train_variables + [key_variable, to_predict, "Age"]))
    kernel = 'rbf'

    # Train the SPARE model using the specified parameters
    results = sp.spare_train(
        data, 
        to_predict,
        predictor_type,
        positive_group,
        key_variable,
        train_variables,
        ignore_variables,
        kernel,
        output_model_path
    )

    return results

def model_test(data_path_test, model_path, output_path=''):
    """
    Test a SPARE model using the specified test data and save the results to the specified path.

    Args:
        data_path_test (str): Path to the CSV file containing the test data.
        model_path (str): Path to the saved model file.
        output_path (str, optional): Path to save the test results. Defaults to ''.

    Returns:
        dict: Results of the testing process.
    """
    results = sp.spare_test(data_path_test, model_path, output=output_path)

    return results