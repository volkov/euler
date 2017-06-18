def poly(n):
  nstr = str(n)
  l = len(nstr)
  for i in range(0,l/2):
    if nstr[i]!=nstr[l-1-i]:
      return False
  return True

largest = 1
for i in range(100,999):
  for j in range(100,999):
    m = i*j
    if m>largest and poly(m):
      largest = m
print largest
