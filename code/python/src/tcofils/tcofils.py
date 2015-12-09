# -*- coding: utf-8 -*-
#!/usr/bin/env python

import numpy as np
import scipy as sp
import sys

from sklearn.preprocessing import scale,OneHotEncoder
from sklearn.utils.extmath import randomized_svd
from src.lib.array import num_nonzero_elements as qtty_nonzeros
from src.lib.array import replace_zero_elements as replace_zeros
from src.lib.array import subtract_nonzero_elements as subtract_nonzeros
from src.lib.date import get_day_of_week_from_timestamp
from src.tcofils.random_forest import random_forest_regressor

def generate_sl_dataset(
    ratings_matrix,
    normalization_method="user_avg",
    factorization_method="svd",
    num_factors=2,
    include_time=False):
    
    preference_matrix = _build_preference_matrix(ratings_matrix)

    if normalization_method == "user_avg":
        normalized_preference_matrix = _normalize_user_avg(preference_matrix)
    elif normalization_method == "item_avg":
        normalized_preference_matrix = _normalize_item_avg(preference_matrix)
    else:
        raise ValueError("Bad normalization_method: {0}. Supported values:\"user_avg\",\"item_avg\".".format(normalization_method))

    if factorization_method=="svd":
        sl_dataset = _generate_dataset_svd(
            normalized_preference_matrix,
            num_factors=num_factors,
            ratings_matrix=ratings_matrix,
            include_time=include_time)
    else:
        raise ValueError("Bad factorization_method: {0}. Supported values:\"svd\".".format(factorization_method))    

    return(sl_dataset)

def apply_random_forest_regressor(dataset,num_trees=10,num_folds=2):
    
    mae,rmse = random_forest_regressor(dataset,num_trees,num_folds)

    return(mae,rmse)

def _generate_dataset_svd(preference_matrix,num_factors,ratings_matrix,include_time):
    
    # returns the top factors
    U,_,VT = randomized_svd(preference_matrix,n_components=num_factors,n_iter=5)

    # will use a regular list to make looping faster
    sl_dataset_list = []

    if (include_time == "naive") or (include_time == False):
        pass # just leave it as is
    elif include_time == "standardized":    
        ratings_matrix[:,3] = scale(ratings_matrix[:,3])
    elif include_time == "weekday":
        v_func = np.vectorize(get_day_of_week_from_timestamp)
        day_indices = np.apply_along_axis(v_func,0,ratings_matrix[:,3]).reshape(-1,1)
        # categorical features need to be one-hot encoded
        enc = OneHotEncoder(sparse=False)
        enc.fit(day_indices)
        # remove the timestamps from the dataset,we will replace them with the OHE-array
        ratings_matrix = np.delete(ratings_matrix,-1,1)

        one_hot_vecs = enc.transform(day_indices)

        # print(one_hot_vecs)
        # sys.exit()

        ratings_matrix = np.hstack( (ratings_matrix,one_hot_vecs) )

    for row in ratings_matrix:
        user_id = int(row[0])
        item_id = int(row[1])
        rating = row[2]
        timestamp = row[3:].tolist()

        # note that entry Aij in the preference matrix refers to user i+1 and to item j+1
        # this is due to the fact that array indices start at 0 while ids at 1
        user_factor_index = user_id-1
        item_factor_index = item_id-1

        user_factor = U[user_factor_index,:].tolist()
        item_factor = VT.T[item_factor_index,:].tolist()

        if not (include_time == False):
            sl_dataset_list.append( [rating]+user_factor+item_factor+timestamp )
        else:
            # don't include time
            sl_dataset_list.append( [rating]+user_factor+item_factor )
    
    sl_dataset = np.array(sl_dataset_list)    

    return(sl_dataset)

def _build_preference_matrix(ratings_matrix):

    max_user_id = int(ratings_matrix[:,0].max())
    max_item_id = int(ratings_matrix[:,1].max())

    preference_matrix = np.zeros((max_user_id,max_item_id))

    for row in ratings_matrix:
        user_id  = int(row[0])
        item_id  = int(row[1])
        rating   = row[2]

        preference_matrix[(user_id-1),(item_id-1)] = rating

    return(preference_matrix)

def _normalize_user_avg(input_matrix):

    output_matrix = np.copy(input_matrix)

    user_sums = np.sum(input_matrix,axis=1)

    number_of_items_rated_by_each_user = np.apply_along_axis(qtty_nonzeros,1,input_matrix)

    user_avgs = user_sums / number_of_items_rated_by_each_user

    for i in range(0,input_matrix.shape[0]):
        output_matrix[i,:] = subtract_nonzeros(input_matrix[i,:],user_avgs[i])

    return(output_matrix)    

def _normalize_item_avg(input_matrix):

    output_matrix = np.copy(input_matrix)

    item_sums = np.sum(input_matrix,axis=0)

    number_of_users_that_rated_each_item = np.apply_along_axis(qtty_nonzeros,0,input_matrix)

    item_avgs = item_sums / number_of_users_that_rated_each_item

    for i in range(0,input_matrix.shape[1]):
        output_matrix[:,i] = subtract_nonzeros(input_matrix[:,i],item_avgs[i])

    return(output_matrix)    
