# -*- coding: utf-8 -*-
#!/usr/bin/env python

import numpy as np
import scipy as sp

from src.lib.numpy import num_non_zero_elements as qtty_nonzero
from src.lib.numpy import replace_zero_elements as replace_zero


def generate_dataset(
    ratings_matrix,
    normalization_method="user_avg",
    method="svg",
    num_factors=2,
    include_time=False):
    
    max_user_id = int(ratings_matrix[:,0].max())
    max_item_id = int(ratings_matrix[:,1].max())

    preference_matrix = np.zeros((max_user_id,max_item_id))

    for row in ratings_matrix:
        user_id  = int(row[0])
        item_id  = int(row[1])
        rating   = row[2]

        preference_matrix[(user_id-1),(item_id-1)] = rating

    if normalization_method == "user_avg":
        normalized_preference_matrix = _normalize_user_avg(preference_matrix)
    elif normalization_method == "item_avg":
        normalized_preference_matrix = _normalize_item_avg(preference_matrix)
    else:
        raise ValueError("Bad normalization method: {0}".format(normalization_method))

    return(normalized_preference_matrix)

def _normalize_user_avg(input_matrix):

    output_matrix = np.copy(input_matrix)

    user_sums = np.sum(input_matrix,axis=1)

    number_of_items_rated_by_each_user = np.apply_along_axis(qtty_nonzero,1,input_matrix)

    user_avgs = user_sums / number_of_items_rated_by_each_user

    for i in range(0,input_matrix.shape[0]):
        output_matrix[i,:] = replace_zero(input_matrix[i,:],user_avgs[i])

    return(output_matrix)    

def _normalize_item_avg(input_matrix):

    raise ValueError("Not implemented yet. Use _normalize_user_avg instead.")

    # non_zeros = lambda column: len(filter(lambda elem: elem != 0,column))

    # item_rating_sums = np.sum(input_matrix,axis=0)

    # number_of_users_who_rated_each_item = non_zeros(input_matrix.T)

    # assert(len(number_of_users_who_rated_each_item) == input_matrix.shape[1])

    # item_avgs = item
