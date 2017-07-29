ss=0
for n in range(2,1000000):
    i=n
    s=0
    while i:
       s+=(i%10)**5
       i//=10
    if s==n:
        print(s)
        ss+=s
print("total",ss)
