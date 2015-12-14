import numpy as np

from sklearn.preprocessing import scale,OneHotEncoder
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
            "standardized",
            "day_of_week",
            "day_of_month",
            "am_pm"       
    """
    if strategy == False:
        return(_identity(column))
    else:
        if strategy == "naive":
            return(_naive(column))
        elif strategy == "standardized":
            return(_standardized(column))
        elif strategy == "day_of_week":
            return(_day_of_week(column))
        elif strategy == "day_of_month":
            return(_day_of_month(column))
        elif strategy == "am_pm":
            return(_am_pm(column))   
        else:
            raise ValueError("Invalid strategy: {0}".format(strategy))          

def _identity(column):
    return(column.reshape(-1,1))
    
def _naive(column):
    return(column.reshape(-1,1))

def _standardized(column):
    return(scale(column).reshape(-1,1))

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


