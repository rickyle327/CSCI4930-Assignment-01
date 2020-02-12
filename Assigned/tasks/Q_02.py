def Q_02(self):
    # Task 2: Return a list of of two numbers: [n0, n1], where
    # n0 represents number of class=0 (negative) samples and n1 represents number of class=1 (positive) samples
    # in the validation dataset: "dataset/validation.csv"
    n0 = 0
    n1 = 0

    # YOUR CODE HERE
    column = list(self.validation.iloc[:, 8])
    for i in column:
        if i == 0:
            n0 += 1
        elif i == 1:
            n1 += 1

    return [n0, n1]
