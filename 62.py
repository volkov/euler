def normalize(x):
  return "".join(sorted(list(str(x))))
i = 1
counts={}
while True:
  cube = i**3
  n = normalize(cube)
  l = counts.get(n,[])
  l.append(cube)
  if len(l)==5:
    print(l)
    print(min(l))
    break
  counts[n] = l
  i+=1 
