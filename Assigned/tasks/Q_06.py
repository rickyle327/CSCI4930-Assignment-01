def accuracy(self, conf_mat):
    # Given a confusion matrix, i.e. the list of four metrics: [TN,FP, FN, TP], in this order
    # return accuracy. In case of Division by Zero error, return -1.
    [TN, FP, FN, TP] = conf_mat

    acc = 0

    # YOUR CODE HERE
    if (TN + FP + FN + TP) == 0:
        return -1

    acc = (TP + TN) / (TN + FP + FN + TP)

    return acc


def Q_06(self):
    # Task 6: Please complete the function "accuracy" above
    pass
