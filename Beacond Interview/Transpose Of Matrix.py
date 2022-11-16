Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]

result= [[0,0,0],
        [0,0,0],
        [0,0,0],
         [0,0,0]
        ]
for i in range(len(Y[0])):
    for j in range(len(Y)):
        result[i][j] = Y[j][i]
        
for i in range(len(result)):
    print(result[i])