def rec(n):
    res=1
    i=1
    resdict={res:i}
    while True:
        i+=1
        numerator=10*res
        res = numerator % n
        if res in resdict:
            return i - resdict[res]
        else:
            resdict[res]=i

print(list(reversed(sorted(map(lambda n: (rec(n),n),range(1,1000))))))
