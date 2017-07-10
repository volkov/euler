def fib():
    pp=0
    yield pp
    p=1
    yield p
    while True:
        n=p+pp
        yield n
        pp=p
        p=n

limit=10**999
for i,f in enumerate(fib()):
    if f >= limit:
        print(i,f)
        quit()
