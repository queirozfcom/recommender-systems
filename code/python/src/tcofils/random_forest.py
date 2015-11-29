
import numpy as np

from math import sqrt
from sklearn import cross_validation
from sklearn.cross_validation import KFold
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

def random_forest_regressor(
    dataset,
    num_trees = 10,
    num_folds = 2):

    n = dataset.shape[0]
    d = dataset.shape[1]

    X = dataset[:, range(1,d)]

    # a variável objetivo precisa ser a coluna zero!!!
    y = dataset[:,0]

    kf = KFold(n,num_folds)

    # MAE and RMSE before averaging, respectively
    total_MAE  = 0.0
    total_RMSE = 0.0

    # repeat for each fold
    for train_index, test_index in kf:

        X_train = X[train_index]
        y_train = y[train_index]

        X_test  = X[test_index]
        y_test  = y[test_index]

        clf = RandomForestRegressor(n_estimators=num_trees, n_jobs=-1)

        clf.fit(X_train,y_train)

        y_predicted = clf.predict(X_test)

        mean_absolute_error = np.abs((y_predicted - y_test)).mean()

        root_squared_error = sqrt(mean_squared_error(y_test, y_predicted))

        total_MAE += mean_absolute_error

        total_RMSE += root_squared_error

    MAE = total_MAE / num_folds
    RMSE = total_RMSE / num_folds

    return(MAE,RMSE)

    


    

