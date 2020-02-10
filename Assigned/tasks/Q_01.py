def Q_01(self):
    #Task 1: Return total number of samples in the validation dataset: "dataset/validation.csv"

    total_number = 0
    ## YOUR CODE HERE ##
    with open("/dataset/validation.csv", 'r') as csvfile:
        for line in csvfile:
            total_number += 1                

    return total_number