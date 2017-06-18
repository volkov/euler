import math
l = 2000000 
primes = [True]*l
s = 0
for i in range(2,l):
  if primes[i]:
    s+=i
    for j in range(i*2,l,i):
      primes[j]=False
print s 
