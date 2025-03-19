import numpy as np
array_1=np.array([2, 3, 4, 5])
array_2=np.array([1, 2, 3, 4])
@np.vectorize
def num_to_pow(a,b):
    return a**b
powered_array=num_to_pow(array_1,array_2)
print(powered_array)