import numpy as np
import pandas as pd
import os.path, sys
import math

def similarity(df,user_avg_df,a_id,b_id):
    """Calculates the similarity between two movies, a and b

    Args:
        df: training dataframe
        a_id: movie a item_id
        b_id: movie b item_id    
    Returns:
        float, similarity between a and b
    """

    # the similarity between two movies is given by:
    #
    # the sum, over all users who have rated both a and b, of the difference between the rating given to movies a and b and the average rating that user has given for all movies
    # divided by
    # the square root of 
    #  (the sum of the difference between the rating user u gave to movie a and the avg of user u's ratings)
    #   times
    #  (the sum of the difference between the rating user u gave to movie b and the avg of user u's ratings)

    # rows for users that have rated a
    a_df = df[ df["item_id"] == a_id ]
    # rows for users that have rated b
    b_df = df[ df["item_id"] == b_id ]
    # rows for users who have rated both
    ab_df = a_df.merge(b_df,on="user_id")

    unique_user_ids = np.unique(ab_df["user_id"].values)

    numerator = 0.0
    denominator_left = 0.0
    denominator_right = 0.0

    # print("{0} users have rated both a and b".format(len(unique_user_ids)))

    for user_id in unique_user_ids:
        user_avg = user_avg_df[ user_avg_df["user_id"] == user_id]["rating_avg"].values[0]

        rating_a = a_df[ a_df["user_id"] == user_id]["rating"].values[0]
        rating_b = b_df[ b_df["user_id"] == user_id]["rating"].values[0]

        numerator += ( (rating_a - user_avg)*(rating_b - user_avg) )
        denominator_left += (rating_a - user_avg) ** 2
        denominator_right += (rating_b - user_avg) ** 2

    denominator = math.sqrt(denominator_left + denominator_right)

    if denominator == 0.0:
        res = 0.0
    else:
        res = numerator / denominator

    # print("res is {0} \n".format(res))
    return(res)            

def main():
    data_dir = os.path.join(sys.path[0],'../../data/ml-100k/ml-100k/')

    target_file = data_dir+'u1.base.item_similarity'

    train_df = pd.read_csv(data_dir+'u1.base',sep='\t',names=["user_id","item_id","rating","timestamp"]).drop(["timestamp"],1)
    user_avg_df = pd.read_csv(data_dir+'u1.base.user_avgs',names=["user_id","rating_avg"])

    unique_item_ids = np.unique(train_df["item_id"].values)

    sim_rows = []

    for i in unique_item_ids:
        row = dict()
        for j in unique_item_ids:
            row[j] = similarity(train_df,user_avg_df,i,j)

        sim_rows.append(row)

    sim_df = pd.DataFrame(sim_rows) 

    sim_df.to_csv(target_file)

if __name__ == '__main__':
    main()