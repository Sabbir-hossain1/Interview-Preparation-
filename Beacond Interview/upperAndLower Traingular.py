matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# find upper and lower triangular values
l = []
lt= []
for i in range(3):
    for j in range(3):
      if i>j:
          l.append(matrix[i][j])
      if i<j:
          lt.append(matrix[i][j])
    
print("Upper and lower  matrixes values : ",l,lt)

# copy upper matrix value to lowermatrix
k= 0
p = 0
for i in range(3):
    for j in range(3):
        if i<j:
            matrix[i][j] = l[k]
            k = k+1
        if i>j:
            matrix[i][j] = lt[p]
            p = p+1

# print matrix
for i in range(3):
    print(matrix[i])
