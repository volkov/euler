from divisors import gcd
L=1000000
n0=3
d0=7
mindiff=1
for d in range(1,L+1):
    n = d*n0//d0
    if d%d0==0:
        n-=1
    diff = n0/d0-n/d
    #print(n,d)
    #print(diff)
    
    if diff<mindiff:
        mindiff = diff
        res = (n,d)
print(res)
g = gcd(res[0],res[1])
print(res[0]/g,res[1]/g)
print(mindiff)
