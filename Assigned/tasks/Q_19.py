def Q_19(self, model_file="models/Model_1.pkl"):
    # Task 19: Flip the prediction of Model 1, and then compute and
    #  return as a dataframe containing:
    #      {acc,prec,rec,f1,mcc,FDR} on the
    #   original (i.e., not-scaled) validation dataset: "dataset/validation.csv"
    #     # You can load the pretrained model via pickle library. Here is an example use:
    #     # infile = open('pickle-file.pkl','rb')
    #     # model = pickle.load(infile)
    #     # infile.close()
    #     # y_pred = model.predict(X) #to get the predictions of all the X samples using the model
    import pickle
    import sys
    import os
    import numpy as np
    import pandas as pd
    from sklearn.linear_model import LogisticRegression
    from sklearn.neural_network import MLPClassifier
    from sklearn import tree
    from sklearn.svm import SVC
    from sklearn.neighbors import KNeighborsClassifier

    acc = 0
    prec = 0
    rec = 0
    f1 = 0
    mcc = 0
    fdr = 0

    ## YOUR CODE HERE ##
    y_actual = self.validation.iloc[:, 8].tolist()
    with open(model_file, 'rb') as infile:
        model = pickle.load(infile)
        y_pred = model.predict(self.validation.drop(self.validation.columns[8], axis='columns')).tolist()
        swap = {0: 1, 1: 0}
        for i in range(0, len(y_pred)):
            y_pred[i] = swap[y_pred[i]]

        conf_mat = self.confusion_matrix(y_actual, y_pred)
        acc = self.accuracy(conf_mat)
        prec = self.precision(conf_mat)
        rec = self.recall(conf_mat)
        f1 = self.F1(conf_mat)
        mcc = self.MCC(conf_mat)
        fdr = self.FDR(conf_mat)
        result = pd.DataFrame({'Accuracy': [acc], 'Precision': [prec], 'Recall': [rec], 'F1': [f1], 'MCC': [mcc], 'FDR': [fdr]})

    return result