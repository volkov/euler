def good_fractions(x):
    a=[int(x**0.5)]
    b=[1]
    c=[a[0]]
    
    pp=[a[0]]
    qq=[1]

    yield (pp[0],qq[0])
    i=0
    while True:
        i+=1
        p=i-1
        a.append(int(b[p]/(x**0.5-c[p])))
        b.append((x-c[p]**2)/b[p])
        c.append(-(b[p]*c[p]-a[i]*x+a[i]*c[p]**2)/b[p])
        if (i>1):
            pp.append(a[i]*pp[i-1]+pp[i-2])
            qq.append(a[i]*qq[i-1]+qq[i-2])
        else:
            pp.append(a[i]*pp[i-1]+1)
            qq.append(a[i]*qq[i-1])
        yield (pp[i],qq[i])


def solution(D):
    for i,(p,q)in enumerate(good_fractions(D)):
        if p**2-D*q**2==1:
            return (p,q)
maxx=0
maxD=0
for D in range(2,1001):
    if not (D**0.5).is_integer():
        s = solution(D)
        x=s[0]
        if x>maxx:
            maxD=D
            maxx=x
        print("%d^2-%d*%d^2=1"%(x,D,s[1]))
print(maxx)
print(maxD)
