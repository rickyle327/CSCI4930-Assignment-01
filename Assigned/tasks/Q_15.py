def Q_15(self):
    # Task 15: Scale the all the features of the validaton set using the formula, z = (x-m)/s,
    #   where m = mean of a feature in the training set: "dataset/training.csv"
    #         s = standard deviation of the feature in the training set: "dataset/training.csv"
    #  DO NOT SCALE the target feature.
    # At the end, return a tuple (X, y), with X being a numpy array of shape (N,8) and y is an N dim array
    # and N is the total number of samples in the validation set: "dataset/validation.csv".

    X = None
    y = None

    # YOUR CODE HERE
    import numpy as np
    y = list(self.validation.iloc[:, 8])
    X = self.validation.drop(self.validation.columns[8], axis='columns').to_numpy()
    for c in range(0, len(X[0])):
        feature = list(self.training.iloc[:, c])
        m = np.mean(feature)
        s = np.std(feature)
        X[c] = X[c].astype(float)
        for r in range(0, self.validation.count(axis='columns').values.size):
            X[r][c] = (X[r][c] - m) / s

    return (X, y)
