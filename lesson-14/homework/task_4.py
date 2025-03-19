import numpy as np
coefficients=np.array([[10, -2, 3], [-2, 8, -1], [3, -1, 6]])
results=np.array([12, -5, 15])
I1_I2_I3=np.linalg.solve(coefficients,results)
print("I1_I2_I3 =",I1_I2_I3)