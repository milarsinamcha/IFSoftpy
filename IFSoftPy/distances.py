

def ifss_hamming_distance(ifss1, ifss2):
    m = ifss1.membership_values.shape[1]  # Number of elements in the array
    if ifss1.membership_values.shape[1] != ifss2.membership_values.shape[1]:
        raise ValueError("Number of elements in the sets must be the same for comparison.")
    else:
        vm1 = np.absolute(ifss1.membership_values - ifss1.non_membership_values)
        vm2 = np.absolute(ifss2.membership_values - ifss2.non_membership_values)
        distance = np.sum(vm1 - vm2)
        return distance / (2 * m)

def ifss_normalized_hamming_distance(ifss1, ifss2):
    n = ifss1.membership_values.shape[0]  # Number of arrays
    m = ifss1.membership_values.shape[1]  # Number of elements in the array

    if ifss1.membership_values.shape != ifss2.membership_values.shape:
        raise ValueError("Shapes of membership_values must be the same for comparison.")

    vm1 = np.absolute(ifss1.membership_values - ifss1.non_membership_values)
    vm2 = np.absolute(ifss2.membership_values - ifss2.non_membership_values)
    distance = np.sum(vm1 - vm2)
    return distance / (2 * m * n)

def ifss_euclidean_distance(ifss1, ifss2):
    m = ifss1.membership_values.shape[1]  # Number of elements in the array
    if ifss1.membership_values.shape[1] != ifss2.membership_values.shape[1]:
        raise ValueError("Number of elements in the sets must be the same for comparison.")
    else:
        vm1 = np.absolute(ifss1.membership_values - ifss1.non_membership_values)
        vm2 = np.absolute(ifss2.membership_values - ifss2.non_membership_values)
        distance = (np.sum(np.square(vm1 - vm2)))**(1/2)
        return distance / (2 * m)
    
def ifss_normalized_euclidean_distance(ifss1, ifss2):
    n = ifss1.membership_values.shape[0]  # Number of arrays
    m = ifss1.membership_values.shape[1]  # Number of elements in the array
    if ifss1.membership_values.shape[1] != ifss2.membership_values.shape[1]:
        raise ValueError("Number of elements in the sets must be the same for comparison.")
    else:
        vm1 = np.absolute(ifss1.membership_values - ifss1.non_membership_values)
        vm2 = np.absolute(ifss2.membership_values - ifss2.non_membership_values)
        distance = (np.sum(np.square(vm1 - vm2)))**(1/2)
        return distance / (2 * m *n)
