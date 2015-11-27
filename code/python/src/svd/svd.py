# -*- coding: utf-8 -*-

import os, sys
import numpy as np
import scipy.sparse as sps
import csv

def main():
    data_dir = os.path.join(sys.path[0],'../../data/ml-100k/ml-100k/')

    train_data = np.genfromtxt(data_dir+'u1.base', delimiter='\t')
    # tirar a coluna de timestamp
    train_data = np.delete(train_data,-1,1)

    test_data = np.genfromtxt(data_dir+'u1.test', delimiter='\t')
    test_data = np.delete(test_data,-1,1)

    users = train_data[:,0]
    items = train_data[:,1]
        
    A = np.zeros(  int(users.max())*int(items.max()) ).reshape((int(users.max()),int(items.max())))

    # element (i,j) refers to user i+1 and item j+1
    for row in train_data:
        user_id,item_id,rating = row
   
        A[int(user_id-1),int(item_id-1)] = rating

    global_item_average = items.mean()    

    # let's use the item averages to fill missing values
    item_averages = np.zeros(int(items.max()))

    for (item_id,column) in enumerate(A.T):
        nonzeros = np.array(list(filter(lambda elem: elem != 0.0,column)))
    
        # if the item hasn't been rated yet, assign it the global average 
        if(len(nonzeros)==0):
            item_avg = global_item_average
        else:
            item_avg = nonzeros.mean()
    
        item_averages[item_id-1] = item_avg
    
    # SVD algorithm is applied here
    user_component,s,item_component = np.linalg.svd(A,full_matrices=False)


    SE = 0.0

    # reconstructed matrix
    A_hat = np.dot(np.dot(user_component,np.diag(s)),item_component)

    # checking our predictions
    for row in test_data:
        user_id = int(row[0])
        item_id = int(row[1])
        rating = row[2]
        
        i = user_id-1
        j = item_id-1
        
        user_feature_vector = user_component[i]
        item_feature_vector = item_component.T[j]
       
        rating_hat = A_hat[i][j]

        squared_error = (rating - rating_hat) ** 2
        
        SE += squared_error
        
    MSE = SE/len(test_data)
    RMSE = np.sqrt(MSE)
    print("Got {0} for RMSE".format(RMSE))    

if __name__ == '__main__':
    main()