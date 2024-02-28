import numpy as np
from . import ifss_hamming_distance, ifss_normalized_hamming_distance, ifss_euclidean_distance, ifss_normalized_euclidean_distance
from .sets import IntuitionisticFuzzySoftSet

def ifss_similarity_Muthukumar_Sundara(ifss1, ifss2):
    """ 
    Similarity measure prosposed by : P. Muthukumar , G.Sai Sundara Krishnan
    """
    if ifss1.membership_values.shape[1] != ifss2.membership_values.shape[1]:
        raise ValueError("Number of elements in the sets must be the same for comparison.")
    else:
        numerator = np.sum((ifss1.membership_values * ifss2.membership_values) +
                           (ifss1.non_membership_values * ifss2.non_membership_values))
        denominator = np.sum(
            np.maximum(ifss1.membership_values**2, ifss2.membership_values**2) +
            np.maximum(ifss1.non_membership_values**2, ifss2.non_membership_values**2)
        )
        return numerator / denominator
    
def ifss_similarity_Rajarajeswari_Dhanalakshmi_matching_function(ifss1, ifss2):
    """
    Similarity measure of IFSS based on matching function proposed by P. Rajarajeswari and P. Dhanalakshmi
    """
    if ifss1.membership_values.shape[1] != ifss2.membership_values.shape[1]:
        raise ValueError("Number of elements in the sets must be the same for comparison.")
    else:
        vm1=np.absolute(ifss1.membership_values - ifss1.non_membership_values)
        vm2=np.absolute(ifss2.membership_values - ifss2.non_membership_values)
        numerator = np.sum(vm1 * vm2)
        denominator = np.sum(
            np.maximum(vm1**2, vm2**2) )
        return numerator / denominator

def ifss_similarity_Rajarajeswari_Dhanalakshmi_set_theory(ifss1, ifss2):
    """
    Similarity measure of IFSS based on set theoretic approach P. Rajarajeswari and P. Dhanalakshmi
    """
    max_similarity = 0.0

    for i in range(ifss1.membership_values.shape[0]):
        new_membership_infss1 = np.array(ifss1.membership_values[i])
        new_non_membership_infss1 = np.array(ifss1.non_membership_values[i])
        new_membership_infss2 = np.array(ifss2.membership_values[i])
        new_non_membership_infss2 = np.array(ifss2.non_membership_values[i])
        new_ifss1 = IntuitionisticFuzzySoftSet(new_membership_infss1, new_non_membership_infss1)
        new_ifss2 = IntuitionisticFuzzySoftSet(new_membership_infss2, new_non_membership_infss2)

        vm1 = np.absolute(new_ifss1.membership_values - new_ifss1.non_membership_values)
        vm2 = np.absolute(new_ifss2.membership_values - new_ifss2.non_membership_values)
        numerator = np.sum(np.minimum(vm1, vm2))
        denominator = np.sum(np.maximum(vm1, vm2))
        similarity = numerator / denominator
        max_similarity = max(max_similarity, similarity)

    return max_similarity

def ifss_similarity_on_distance(ifss1, ifss2, distance_type):
    if distance_type == 'ifss_hamming_distance':
        distance = ifss_hamming_distance(ifss1, ifss2)
    elif distance_type == 'ifss_normalized_hamming_distance':
        distance = ifss_normalized_hamming_distance(ifss1, ifss2)
    elif distance_type == 'ifss_euclidean_distance':
        distance = ifss_euclidean_distance(ifss1, ifss2)
    elif distance_type == 'ifss_normalized_euclidean_distance':
        distance = ifss_normalized_euclidean_distance(ifss1, ifss2)
    else:
        raise ValueError("Invalid distance type. Supported types: 'ifss_hamming_distance', 'ifss_normalized_hamming_distance', 'ifss_euclidean_distance', 'ifss_normalized_euclidean_distance'")

    return 1 / (1 + distance)
