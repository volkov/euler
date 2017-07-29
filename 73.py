from divisors import gcd

D=12000
bottom = (1,3)
top = (1,2)

values = set()
for d in range(4,D+1):
    minn=d*bottom[0]//bottom[1]
    minn+=1
    maxn = d*top[0]//top[1]
    if d%top[1]==0:
        maxn-=1
    for n in range(minn,maxn+1):
        g = gcd(n,d)
        values.add((n//g,d//g))
print(len(values))
