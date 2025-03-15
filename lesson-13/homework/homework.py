import numpy as np
from random import randint
import random
# Q1
v1 = np.arange(10,50)
# Q2
l2 = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
v2 = np.array(l2)
# Q3
v3 = np.eye(3,)
# Q4
v4 = [
    [
        [3,5,1],
        [2,4,4],
        [7,9,0]
    ],
    [
        [1,2,8],
        [0,9,4],
        [5,5,7]
    ],
    [
        [6,5,8],
        [3,1,1],
        [7,7,4]
    ]
]
# Q5
v5 = np.random.randint(0, 100, (10,10))
max5 = v5.max()
min5 = v5.min()
# Q6
v6 = np.random.randint(0, 500, (30,))
mean6 = v6.mean()
# Q7
v7 = np.random.randint(0,100, (5,5))
min7 = v7.min()
max7 = v7.max()
norm7 = (v7-min7)/(max7-min7)
# Q8
v8_1 = np.random.randint(0,50, (5,3))
v8_2 = np.random.randint(0,50, (3,2))
v8_result = np.dot(v8_1,v8_2)
# Q9
v9_1 = np.random.randint(0, 10, (3,3))
v9_2 = np.random.randint(0, 10, (3,3))
v9_result = np.dot(v9_1, v9_2)
# Q10
v10 = np.random.randint(0,20, (4,4))
v10_transpose = np.transpose(v10)
# Q11
v11 = np.random.randint(0,20, (3,3))
v11_determinant = np.linalg.det(v11)
# Q12
v12_A = np.random.randint(0,20, (3,4))
v12_B = np.random.randint(0,20, (4,3))
v12_result = np.dot(v12_A, v12_B)
# Q13
v13_1 = np.random.randint(0,20, (3,3))
v13_2 = np.random.randint(0,10, (3,1))
v13_result = np.dot(v13_1, v13_2)
# Q14
v14_A = np.random.randint(0,20, (3,3))
v14_b = np.random.randint(0,10, (3,1))
v14_solution = np.linalg.solve(v14_A, v14_b)
# Q15
v15 = np.random.randint(0,50, (5,5))
v15_row_wise = v15.sum(axis=1)
v15_column_wise = v15.sum(axis=0)