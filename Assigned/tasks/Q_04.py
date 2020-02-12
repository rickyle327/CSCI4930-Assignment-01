def Q_04(self):
    # Task 4: Return median (i.e., 50% percentile) of the seventh feature: "'U' frequencies of sequence 2" of
    # the validation dataset: "dataset/validation.csv"

    med = 0

    ## YOUR CODE HERE ##
    import numpy as np
    column = list(self.validation.iloc[:, 6])
    med = np.median(column)

    return med


