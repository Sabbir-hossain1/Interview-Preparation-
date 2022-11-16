# Solution 1
mat = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
# for i in range(len(mat)):
#     if i % 2 == 0:
#         print(mat[i])
#     else:
#         l = []
#         for j in range(len(mat[i])-1,-1,-1):
#             l.append(mat[i][j])
#         print(l)

# Solution 2
for i in range(len(mat)):
    k= len(mat[0])-1
    for j in range(len(mat[0])):
        if i % 2!=0:
            print(mat[i][k],end=" ")
            k = k-1
        else:
            print(mat[i][j],end=' ')
            
    print()