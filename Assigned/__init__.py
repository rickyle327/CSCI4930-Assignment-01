class Assigned:
    def __init__(self, training_filename, validation_filename, target_column_index):
        self.training_filename =training_filename
        self.target_column =target_column_index
        import pandas as pd
        # First load the dataset into pandas dataframe
        self.training = pd.read_csv(training_filename,header=None,delimiter=',')
        self.validation = pd.read_csv(validation_filename,header=None,delimiter=',')




    #Imported methods
    from .tasks.Q_01 import Q_01
    from .tasks.Q_02 import Q_02
    from .tasks.Q_03 import Q_03
    from .tasks.Q_04 import Q_04
    from .tasks.Q_05 import Q_05, confusion_matrix
    from .tasks.Q_06 import Q_06, accuracy
    from .tasks.Q_07 import Q_07, precision
    from .tasks.Q_08 import Q_08, recall
    from .tasks.Q_09 import Q_09, F1
    from .tasks.Q_10 import Q_10, MCC
    from .tasks.Q_11 import Q_11, FDR
    from .tasks.Q_12 import Q_12
    from .tasks.Q_13 import Q_13
    from .tasks.Q_14 import Q_14
    from .tasks.Q_15 import Q_15
    from .tasks.Q_16 import Q_16
    from .tasks.Q_17 import Q_17
    from .tasks.Q_18 import Q_18
    from .tasks.Q_19 import Q_19
    from .tasks.Q_20 import Q_20




















