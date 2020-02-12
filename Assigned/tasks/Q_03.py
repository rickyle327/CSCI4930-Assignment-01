def Q_03(self):
    # Task 3: Return standard deviation of the second feature:"The length of shorter sequence" of
    # the validation dataset: "dataset/validation.csv"
    std = 0

    # YOUR CODE HERE
    import numpy as np
    column = list(self.validation.iloc[:, 1])
    std = np.std(column)
    return std


