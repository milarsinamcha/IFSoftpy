import numpy as np

class IntuitionisticFuzzySoftSet:
    def __init__(self, membership_values, non_membership_values):
        self.membership_values = np.asarray(membership_values)
        self.non_membership_values = np.asarray(non_membership_values)