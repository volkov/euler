maxn=0
maxl=0
for i in range(1,1000001):
  iold=i
  if i%100000==0:
    print(".",)
  l = 1
  while i != 1:
    if i%2 == 0:
      i = i // 2
    else:
      i = 3*i + 1
    l+=1
  if l>maxl:
    maxl=l
    maxn=iold
print()
print(maxn)

