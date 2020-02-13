def Q_17(self, performance_result_dataframe):
    # Task 17: Return the model name with path which is performing superior in terms of accuracy, given the
    #  performance result dataframe from Q_16

    name = "models/xxx.pkl"

    ## YOUR CODE HERE ##
    sample = performance_result_dataframe.loc[performance_result_dataframe['Accuracy'].idxmax()]
    name = sample.get(key='model_name')

    return name