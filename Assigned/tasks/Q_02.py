def Q_02(self):
    #Task 2: Return a list of of two numbers: [n0, n1], where
    # n0 represents number of class=0 (negative) samples and n1 represents number of class=1 (positive) samples
    # in the validation dataset: "dataset/validation.csv"
    n0 = 0
    n1 = 0

    ## YOUR CODE HERE ##
    with open("/dataset/validation.csv", 'r') as csvfile:
        for line in csvfile:
            sample = line.split(',')
            if sample[8] == 0:
                n0 += 1
            elif sample[8] == 1:
                n1 += 1

    return [n0, n1]