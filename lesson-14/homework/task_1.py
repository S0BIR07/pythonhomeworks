import numpy as np
array=np.array([32, 68, 100, 212, 77])
@np.vectorize
def fahrenheit_to_celsius(F):
    return (F-32)*5/9
celsius_array=fahrenheit_to_celsius(array)
print(celsius_array)