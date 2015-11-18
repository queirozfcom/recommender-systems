# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import os.path, sys
import math

# add the root folder to sys.path
# sys.path.insert(1, os.path.join(sys.path[0], '../..'))

# from pythoncode.lib import onehot

def item_based_knn(train_df,test_df,user_avg_df, similarity_df,k=3,split=0.8):
    """Calculates the accuracy (RMSE) of predictions that a user U gives
       about item (movie) A.

    Args:
        train_df: training dataframe
        test_df: test dataframe 
        k: the number of neighbours to use, default=3
        split: the proportion of the dataset to use for training, default=0.8
    Returns:
        RMSE Root mean squared error between predictions and actual ratings
    """  
    
    # initial predictions
    test_df["rating_hat"] = None

    # this will be averaged over all rows to get the RMSE
    total_RSE = 0.0

    for index,row in test_df.iterrows():
        item_id = row.loc["item_id"]
        user_id = row.loc["user_id"]

        # using train_df to get the 
        pairs = get_neighbors(train_df,item_id,similarity_df,k)

        sum_weighted_ratings = 0.0
        sum_similarities = 0.0

        for item_id,similarity in pairs:
            rating = train_df.loc[item_id,"rating"]
            weighted_rating =  rating * similarity

            sum_weighted_ratings += weighted_rating
            sum_similarities += similarity

        prediction = sum_weighted_ratings / sum_similarities    

        test_df.loc[item_id,"rating_hat"] = prediction
        original_rating = test_df.loc[item_id,"rating"]

        RSE = math.sqrt( (prediction - original_rating) ** 2 )

        total_RSE += RSE

        # append to the results file
        with open("results.csv","a") as results_file:
            line = "{0},{1},{2},{3},{4}\n".format(user_id,item_id,original_rating,prediction,RSE)
            results_file.write(line)   

        print("For item_id {0}, rating_hat is {1} and original rating was {2}, RSE is {3}".format(item_id,prediction,original_rating,RSE))    

    RMSE = total_RSE / len(test_df)
    
    return(RMSE)    

def get_neighbors(df,item_id,similarity_df,k):
    """

    Returns:
        [(item_id,similarity)]
    """

    # no need to get duplicate values, just unique ones
    dummy_df = pd.DataFrame(df["item_id"].drop_duplicates())
    dummy_df["similarity"] = None

    for index,row in df.iterrows():
        item_id_to_compare = row.loc["item_id"]
        dummy_df.loc[ dummy_df["item_id"] == item_id_to_compare ,"similarity"] = sim(similarity_df,row.loc["item_id"], item_id)

    top_k_neighbors = dummy_df.sort_values("similarity",ascending=False).head(k)
    
    item_ids = top_k_neighbors["item_id"].values
    similarities = top_k_neighbors["similarity"].values

    lst = list(zip(item_ids,similarities))

    return(lst)

def sim(sim_df,item_id_a,item_id_b):

    # the first axis on sim_df is 0-indexed
    try:
        similarity = sim_df.iloc[item_id_a-1][item_id_b]
    except IndexError:
        return(0.0) # missing data

    return(similarity)        

def main():
    data_dir = os.path.join(sys.path[0],'../../data/ml-100k/ml-100k/')

    train_df = pd.read_csv(data_dir+'u1.base',sep='\t',names=["user_id","item_id","rating","timestamp"]).drop(["timestamp"],1)
    test_df = pd.read_csv(data_dir+'u1_c.test',sep='\t',names=["user_id","item_id","rating","timestamp"]).drop(["timestamp"],1)

    user_avg_df =  pd.read_csv(data_dir+'u1.base.user_avgs',names=["user_id","rating_avg"])
    similarity_df = pd.read_csv(data_dir+'u1.base.item_similarity')

    # SANITY TEST
    # for i in range(1,1000):
    #     for j in range(1,1000):
    #         ab = sim(similarity_df,i,j)
    #         ba = sim(similarity_df,j,i)
            
    #         if ab-ba != 0.0:
    #             print("{0} is different from {1}".format(ab,ba))


    # run the algorithm proper
    result = item_based_knn(train_df,test_df,user_avg_df,similarity_df, k=3)

    print("Using K={0}, got RMSE={1:.2f}".format(k,result))


if __name__ == '__main__':
    main()