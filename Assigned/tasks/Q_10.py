def MCC(self, conf_mat):
    # Given a confusion matrix, i.e. the list of four metrics: [TN,FP, FN, TP], in this order
    # return Matthews correlation coefficient (MCC).
    #  In case of Division by Zero error, return -1.
    [TN, FP, FN, TP] = conf_mat
    mcc = 0

    # YOUR CODE HERE
    import numpy as np
    den = np.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
    if den == 0:
        return -1

    mcc = ((TP * TN) - (FP * FN))/den
    return mcc


def Q_10(self):
    # Task 10: Please complete the function "MCC" above
    pass
