import numpy as np

from sklearn.preprocessing import OneHotEncoder,MaxAbsScaler,StandardScaler,MinMaxScaler
from src.lib.date import day_of_week_from_timestamp
from src.lib.date import day_of_month_from_timestamp
from src.lib.date import am_pm_from_timestamp

def transform_time_column(column,strategy):
    """
    Returns:
        a ndarray with some columns and the same number of rows as there 
        are users.

    Args:
        column: the original timestamp column
        strategy: one of:
            False,       
            "naive",
            "standard_scaler",
            "day_of_week_ohe",
            "day_of_month_ohe",
            "am_pm_ohe"

    Note:
        "ohe" stands for one-hot encoding               
    """
    if strategy == False:
        return(_identity(column))
    else:
        if strategy == "naive":
            return(_naive(column))
        elif strategy == "standard_scaler":
            return(_standard_scaler(column))
        elif strategy == "max_abs_scaler":
            return(_max_abs_scaler(column))
        elif strategy == "min_max_scaler":
            return(_min_max_scaler(column))    
        elif strategy == "day_of_week_ohe":
            return(_day_of_week(column))
        elif strategy == "day_of_month_ohe":
            return(_day_of_month(column))
        elif strategy == "am_pm_ohe":
            return(_am_pm(column))   
        else:
            raise ValueError("Invalid strategy: {0}".format(strategy))          

def _identity(column):
    return(column.reshape(-1,1))

def _naive(column):
    return(column.reshape(-1,1))

def _standard_scaler(column):
    sc = StandardScaler()
    sc.fit(column.reshape(-1,1))
    new_col = sc.transform(column.reshape(-1,1))
    return(new_col)

def _max_abs_scaler(column):
    sc = MaxAbsScaler()
    sc.fit(column.reshape(-1,1))
    new_col = sc.transform(column.reshape(-1,1))
    return(new_col)

def _min_max_scaler(column):
    sc = MinMaxScaler()
    sc.fit(column.reshape(-1,1))
    new_col = sc.transform(column.reshape(-1,1))
    return(new_col)

def _day_of_week(column):
    v_func = np.vectorize(day_of_week_from_timestamp)
    day_indices = np.apply_along_axis(v_func,0,column).reshape(-1,1)
    
    # categorical features need to be one-hot encoded
    enc = OneHotEncoder(sparse=False)
    enc.fit(day_indices)

    one_hot_vecs = enc.transform(day_indices)

    return(one_hot_vecs)

def _day_of_month(column):
    v_func = np.vectorize(day_of_month_from_timestamp)
    day_indices = np.apply_along_axis(v_func,0,column).reshape(-1,1)
    
    # categorical features need to be one-hot encoded
    enc = OneHotEncoder(sparse=False)
    enc.fit(day_indices)

    one_hot_vecs = enc.transform(day_indices)

    return(one_hot_vecs)

def _am_pm(column):
    v_func = np.vectorize(am_pm_from_timestamp)
    day_indices = np.apply_along_axis(v_func,0,column).reshape(-1,1)
    
    # categorical features need to be one-hot encoded
    enc = OneHotEncoder(sparse=False)
    enc.fit(day_indices)

    one_hot_vecs = enc.transform(day_indices)

    return(one_hot_vecs)


