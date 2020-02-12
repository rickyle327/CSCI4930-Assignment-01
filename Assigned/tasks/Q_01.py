def Q_01(self):
    # Task 1: Return total number of samples in the validation dataset: "dataset/validation.csv"

    total_number = 0
    # YOUR CODE HERE
    total_number = self.validation.count(axis='columns').values.size

    return total_number
