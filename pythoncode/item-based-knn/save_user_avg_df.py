import numpy as np
import pandas as pd
import os.path, sys
import math

def main():
    data_dir = os.path.join(sys.path[0],'../../data/ml-100k/ml-100k/')

    target_file = data_dir+'u1.base.user_avgs'

    train_df = pd.read_csv(data_dir+'u.data',sep='\t',names=["user_id","item_id","rating","timestamp"]).drop(["timestamp"],1)

    user_avg_df =  train_df.groupby("user_id")["rating"].mean()

    user_avg_df.to_csv(target_file)

if __name__ == '__main__':
    main()