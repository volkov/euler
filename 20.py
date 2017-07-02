from functools import reduce
f = reduce(lambda x,y: x*y,range(1,101))
dsum=0
while f > 0:
  dsum+=f%10
  f=f//10
print(dsum)
