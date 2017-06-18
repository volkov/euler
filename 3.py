import math
n = 600851475143
l = int(math.ceil(math.sqrt(n)))
primes = [True]*l
last = 2
for i in range(2,l):
  if primes[i]:
    if (n%i==0):
      last=i
    for j in range(i*2,l,i):
      primes[j]=False
print last
