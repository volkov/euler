from primes import primes

L = 10000000
K = 1000
primeset = set(primes(L))
maxn=0

for a in range(-K,K):
    for b in range(0,K+1):
        n=0
        while (n**2+a*n+b) in primeset:
            n+=1
        if n > maxn:
            maxn=n
            res = (a,b)
print(res)
print(maxn)
print(res[0]*res[1])

