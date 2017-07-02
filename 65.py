from dsum import dsum
a=[2]
for i in range(1,50):
  a.extend([1,i*2,1])
print(a)
def conv(k):
  d=a[k-1]
  h=1
  for i in range(k-2,-1,-1):
    oldd=d
    d=a[i]*d+h
    h=oldd
  return (d,h)
for i in range(100):
  res = conv(i+1)
  print(i+1,"=",res[0],"/",res[1])

print(dsum(res[0]))
