import numpy as np

def replace_zero_elements(arr,replacement):
    newarr = np.copy(arr)
    newarr[newarr == 0] = replacement

    return(newarr)

def num_non_zero_elements(arr):
   return(len(arr[ arr != 0 ]))