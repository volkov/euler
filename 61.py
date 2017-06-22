from itertools import groupby

min_n=1000
max_n=9999
def accept(n):
  return n<=max_n and n>=min_n
def produce(f):
  return filter(accept,map(f,range(max_n)))
numbers = [
  produce(lambda n: n*(n+1)/2),
  produce(lambda n: n**2),
  produce(lambda n: n*(3*n-1)/2),
  produce(lambda n: n*(2*n-1)),
  produce(lambda n: n*(5*n-3)/2),
  produce(lambda n: n*(3*n-2))
]
print("NUMBERS")
for n in numbers:
  print(n)

nstrings = map(lambda a: map(str,a),numbers)
def h(v):
  return v[:2]
def t(v):
  return v[2:]
N = len(numbers)
nheads = [{} for _ in range(N)]
ntails = [{} for _ in range(N)]
for values,heads,tails in zip(nstrings,nheads,ntails):
  for k,v in groupby(sorted(values,key=h),h):
    heads[k]=set(v)
  for k,v in groupby(sorted(values,key=t),t):
    tails[k]=set(v)
print("TAILS")
for tails in ntails: print(tails)
print("HEADS")
for heads in nheads: print(heads)
def cycle(perm,i=0,stack=[],head=None, tail=None):
  print("Stack on %d is %s" % (i,stack))
  if i==0:
    for x in nstrings[perm[0]]:
      stack.append(x)
      res = cycle(perm,i+1,stack,h(x),t(x))
      if res is not None:
        return res
      stack.pop()
  elif i==N:
    if head==tail:
      return stack
    else:
      return None
  else:
    heads = nheads[perm[i]]
    if tail in heads:
      for x in heads[tail]:
        stack.append(x)
        res = cycle(perm,i+1,stack,head,t(x))
        if res is not None:
          return res
        stack.pop()
def perm(f):
  res = [0]*N
  available = [True]*N
  for i,k in reversed(list(enumerate(f))):
    passed=0
    for j in range(N):
      if available[j]:
        passed+=1
      if passed>k:
        available[j]=False
        res[i]=j
        break
  return res 
f = [0]*N
while True:
  print("RUN %s" % f)
  c = cycle(perm(f))
  if c is not None:
    print("result sequence is %s" % c)
    print("sum is %d" % sum(map(int, c)))
    quit()
  f[0]+=1
  for i,v in enumerate(f):
    if v>i:
      if i == N-1:
        quit()
      else:
        f[i+1]+=1
        f[i]=0
