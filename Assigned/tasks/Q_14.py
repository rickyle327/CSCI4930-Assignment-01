def Q_14(self, performance_result_dataframe):
    # Task 14: Return the model name with path which is performing the worst in terms of recall, given the
    #  performance result dataframe from Q_12
    name = "models/YYYYYY.pkl"

    # YOUR CODE HERE
    sample = performance_result_dataframe.loc[performance_result_dataframe['Recall'].idxmin()]
    name = sample.get(key='model_name')

    return name
