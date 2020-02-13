def Q_20(self):
    # Task 20: Say, in a confusion matrix, the values of the four metrics are: TP=90, TN=1, FP=4, FN=5.
    # Compute F1_original and MCC_original.
    # Now, flip the predictions, i.e., positives are now will be predicted as negative,
    # and negatives are going to be predicted as positive.
    # Then, compute F1_flipped and MCC_flipped.
    # Return the new TP, TN, FP, FN, F1_original,MCC_original,F1_flipped, MCC_flipped, COMMENT
    # as a dataframe, where
    # The COMMENT is a string that will be no longer than 200 characters but is
    #   going to be your comment about the F1 and MCC values for the two cases.

    TP = 0
    TN = 0
    FP = 0
    FN = 0
    COMMENT = "We can see that flipping the predictions will invert the values for f1 and mcc"
    F1_original = 0
    MCC_original = 0
    F1_flipped = 0
    MCC_flipped = 0

    # YOUR CODE HERE
    import pandas as pd
    TP = 90
    TN = 1
    FP = 4
    FN = 5
    conf_mat = [TN, FP, FN, TP]

    F1_original = self.F1(conf_mat)
    MCC_original = self.MCC(conf_mat)

    TP_flipped = FP
    TN_flipped = FN
    FP_flipped = TP
    FN_flipped = TN
    conf_mat_flipped = [TP_flipped, FP_flipped, FN_flipped, TN_flipped]

    F1_flipped = self.F1(conf_mat_flipped)
    MCC_flipped = self.MCC(conf_mat_flipped)

    result = pd.DataFrame({'TP': [5], 'TN': [4], 'FP': [1], \
                           'FN': [90], 'F1_original': [F1_original], \
                           'MCC_original': [MCC_original],'F1_flipped':[F1_flipped],\
                           'MCC_flipped':[MCC_flipped],'COMMENT':[COMMENT]})
    return result
