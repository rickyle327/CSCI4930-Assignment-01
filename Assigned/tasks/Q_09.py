def F1(self, conf_mat):
    # Given a confusion matrix, i.e. the list of four metrics: [TN,FP, FN, TP], in this order
    # return F1 score. It is the harmonic mean of precision and recall.
    #  In case of Division by Zero error, return -1.

    [TN, FP, FN, TP] = conf_mat

    f1 = 0

    # YOUR CODE HERE

    if self.precision(conf_mat) + self.recall(conf_mat) == 0:
        return -1

    f1 = 2 * ((self.precision(conf_mat) * self.recall(conf_mat)) / (self.precision(conf_mat) + self.recall(conf_mat)))

    return f1


def Q_09(self):
    # Task 9: Please complete the function "F1" above
    pass