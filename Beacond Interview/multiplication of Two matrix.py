import numpy as np
a = [[4, 9 ,9],
     [9 ,1, 6],
     [9, 2, 3]
     ]
b = [[2, 2],
     [5 ,7],
     [4 ,4]
     ]
# Write Raw code for multiplication
# Use list comprehension
# use numpy method 1. np.matmul(A,B) 2.use @ operator c = a@b 3. np.dot(A,B)
r = np.dot(a,b)
r1 = np.matmul(a,b)
# print(r)
# print(r1)

# list Comprehension method

# zip(*list) convert colulmn to row
# result = [[sum(a*b for a,b in zip(a_row,b_row)) for b_row in zip(*b)] for a_row in a ]
# print(result)

# Write Raw method

result=[
     [0, 0],
     [0, 0],
     [0, 0]
     ]

for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            result[i][j] += a[i][k] * b[k][j]
print(result)

