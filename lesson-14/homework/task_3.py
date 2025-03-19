import numpy as np
coefficients=np.array([[4, 5, 6], [3, -1, 1], [2, 1, -2]])
results=np.array([7,4,5])
x_y_z=np.linalg.solve(coefficients,results)
print("x,y,z=",x_y_z)