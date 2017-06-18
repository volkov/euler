import math
l = 500000 
primes = [True]*l
n = 0
for i in range(2,l):
  if primes[i]:
    n+=1
    if n==10001:
      print i
      exit 
    for j in range(i*2,l,i):
      primes[j]=False
