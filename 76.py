from primes import primes
maxways=5000
LL = 20000
pl = primes(LL)
L = len(pl)
print("Got {} primes for {}".format(L, LL))
M = [[0] * (LL + 1) for _ in range(L + 1)]
M[0][0] = 1

minj = LL;
for i in range(1, L+1):
    for j in range(0, LL + 1):
        for k in range(j, -1, -pl[i-1]):
            M[i][j] += M[i - 1][k]
        if M[i][j]>maxways:
            if (j<minj):
                print(j,pl[i-1],M[i][j])
                minj = j
