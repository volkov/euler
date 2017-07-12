def primes(l):
    primes = [True]*(l+1)
    primelist = []
    for i in range(2, l+1):
        if primes[i]:
            primelist.append(i)
            for j in range(i * 2, l+1, i):
                primes[j]=False
    return primelist

def prime_normal(x,primes):
    res = {} 
    i=0
    while x>1:
        p = primes[i]
        n = 0
        while x>1 and x%p==0:
            n+=1
            x//=p
        if n>0:
            res[p]=n
        i+=1
    return res

def phi(pn):
    res=1
    for p,n in pn.items():
        if n>0:
            res*=p**n-p**(n-1)
    return res
    
