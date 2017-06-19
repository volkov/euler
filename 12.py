import math
import sys
s = 0
i = 1
while True:
  s += i
  i += 1
  divisor_count = 0
  middle = int(math.sqrt(s))+1
  for j in range(1,middle):
    if s % j ==0:
      divisor_count+=1
      if s//j != j:
        divisor_count+=1 
    if divisor_count > 500:
      print(s)
      sys.exit()
