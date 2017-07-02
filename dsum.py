def dsum(x): 
  dsum=0
  while x > 0:
    dsum+=x%10
    x=x//10
  return dsum
