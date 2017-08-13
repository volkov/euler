L = 100 
M = [[0] * (L + 1) for _ in range(L)]
M[0][0] = 1
for i in range(1, L):
    for j in range(0, L + 1):
        for k in range(j, -1, -i):
            M[i][j] += M[i - 1][k]
#print(M)
print(M[L-1][L])
