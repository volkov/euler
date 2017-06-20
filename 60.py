l = 100000000
z = 9000
primes = [True]*l
primelist = []
for i in range(2, l):
  if primes[i]:
    primelist.append(i)
    for j in range(i * 2, l, i):
      primes[j]=False
def is_prime(x):
  return x<l and primes[x]

def is_good(first, second):
  first_string = str(first)
  second_string = str(second)
  return is_prime(int(first_string+second_string)) and is_prime(int(second_string+first_string))
def add(first, second, matrix):
  if first in matrix:
    matrix[first].add(second)
  else:
    matrix[first]={second}

print(len(primelist))
goodMatrix={}
goodValues=[]
for i in range(0,z):
  prime_i = primelist[i]
  if i%1000==0:
    print('.')
  for j in range(i+1,z):
    prime_j = primelist[j]
    if is_good(prime_i, prime_j):
      add(prime_i, prime_j, goodMatrix) 
      add(prime_j, prime_i, goodMatrix)
      goodValues.append({prime_i, prime_j})
print(len(goodMatrix))
print(goodMatrix[3]&goodMatrix[109]&goodMatrix[7])
for t in range(0,3):
  new_goodvalues=[]
  for values in goodValues:
    intersection = None
    for v in values:
      if intersection is None:
        intersection = goodMatrix[v]
      else:
        intersection = intersection & goodMatrix[v]
        #intersection &= goodMatrix[v]
    if t==1:
      print("{} is intersection for {}".format(intersection, values))
    for i in intersection:
      if values<=goodMatrix[i]:
        new_goodvalues.append(values | {i})
  goodValues = new_goodvalues
print(goodValues)
print(min(map(sum,goodValues)))
