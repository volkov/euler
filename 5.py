def accept(n):
  for i in range(1,20):
    if n%i!=0:
      return False
  return True

i=0
while True:
  i+=20
  if accept(i):
    print i
    break
