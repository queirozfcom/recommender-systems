import numpy as np

def subtract_nonzero_elements(arr,minuend):
    newarr = arr
    np.putmask(newarr,newarr != 0, minuend-newarr)
    return(newarr)

def replace_zero_elements(arr,replacement):
    newarr = np.copy(arr)
    newarr[newarr == 0] = replacement

    return(newarr)

def num_nonzero_elements(arr):
   return(len(arr[ arr != 0 ]))