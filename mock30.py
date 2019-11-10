import numpy as np
mat=np.array([[1,5,6,7],[2,5,9,3],[10,12,4,11]])
m,n=mat.shape
min = 10**9
max = -10**9
for i in range(m):
    for j in range(n):
        if mat[i][j]>= max:
            max=mat[i][j]
        if max<=min:
            min=max
print(min,max)            