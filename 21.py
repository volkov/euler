N=10000
def d(x):
  res=[]
  for i in range(1,max(x//2+1,2)):
    if x%i==0:
      res.append(i)
  return sum(res)
m=[d(i) for i in range(N+1)]
friendly=[]
for i in range(2,N+1):
  if m[i]>i and m[i]<=N and m[m[i]]==i:
    friendly.append(i+m[i])
print(sum(friendly))
