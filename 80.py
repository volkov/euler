from decimal import *
getcontext().prec=110
print(Decimal(2).sqrt())
dsum=0
for i in range(2,100):
    if not (i**0.5).is_integer():
        root = Decimal(i).sqrt()
        if root>10:
            root/=100
        root/=10
        for i in range(100):
            d=int(root*10)
            dsum+=d
            root = root*10-d
print(dsum)

