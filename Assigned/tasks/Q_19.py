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






    result = pd.DataFrame({'Accuracy':[acc],'Precision':[prec],'Recall':[rec],\
                           'F1':[f1],'MCC':[mcc],'FDR':[fdr]})
    return result