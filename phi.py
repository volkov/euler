import primes
L=10**5
pr = primes.primes(L)
prs = pr[:100]
def is_perm(x,y):
    return sorted(list(str(x)))==sorted(list(str(y)))
pp=[0]*(L+1)

for i in range(2,L+1):
    if pp[i]==0:
        pn=primes.prime_normal(i,pr)
        pp[i]=primes.phi(pn)
        for newp in prs:
            j=i*newp
            if j>=L+1:
                break
            if newp in pn:
                pn[newp]=pn[newp]+1
            else:
                pn[newp]=1
            pp[j]=primes.phi(pn)
            pn[newp]=pn[newp]-1

minratio = 10
mini=-1
for i in range(2,L+1):
    p = pp[i]
    if is_perm(i,p):
        print("phi({})={}".format(i,p))
        ratio = i/p
        if ratio<minratio:
            minratio = ratio
            mini=i
print(minratio)
print(mini)
