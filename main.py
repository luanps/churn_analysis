# -*- coding: utf-8 -*-
from sklearn.linear_model import LogisticRegression

from src.utils import load_dataset
from src.exploratory import ExploratoryAnalysis
from src.preproc import Preproc
from src.model import Model

def data_exploration(data):
    exploratory = ExploratoryAnalysis(data)

    print(f"""This dataset contains {exploratory.data_length()[0]}
        samples with {exploratory.data_length()[1]} attributes.\n""")
    print(f"""These attributes are:\n {exploratory.list_attributes()}""")
    print(f"""Attributes with null data:\n {exploratory.check_null()}""")

    empty_spaces = exploratory.check_empty_spaces()
    print(f"""Textual attributes with empty data (value=' '):\n{empty_spaces}""")

    unique_values = exploratory.check_unique_values(10)
    print(f"""Sample of each attribute:""")
    [print(key, value) for key, value in unique_values.items()]
    return empty_spaces


if __name__ == '__main__':
    print("============= Reading data from file  =============")
    filepath = 'data/database.csv'
    data = load_dataset(filepath)

    print("============= Data exploration  =============")
    empty_spaces = data_exploration(data)

    print("============= Applying Preprocessing step =============")
    columns_to_drop = ['customerID','code','Hash']
    preproc = Preproc(data, columns_to_drop, empty_spaces)
    treated_data = preproc.apply_preproc()

    print("============= Data exploration after preprocessing  =============")
    data_exploration(treated_data)

    print("============= Plotting data  =============")
    ExploratoryAnalysis.plot_data(treated_data)

    print("============= Encoding data  =============")
    encoded_data = preproc.encode_data(treated_data)

    print("=============  Running Logistic Regression  =============")
    lr_model = LogisticRegression()
    model_name = 'logistic_regression'
    model = Model(lr_model,model_name)
    model.run_model(encoded_data)
