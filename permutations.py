def perm_from_factorial(f):
    n=len(f)
    res = [0]*n
    available = [True]*n
    for i,k in reversed(list(enumerate(f))):
        passed=0
        for j in range(n):
            if available[j]:
                passed+=1
            if passed>k:
                available[j]=False
                res[i]=j
                break
    return list(reversed(res))

def perms(n):
    f=[0]*n
    while True:
        yield perm_from_factorial(f)
        f[0]+=1
        for i,v in enumerate(f):
            if v>i:
                if i == n-1:
                    return
                else:
                    f[i+1]+=1
                    f[i]=0
