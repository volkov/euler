import math
l = 1000000 
primes = [True]*l
primelist = []
for i in range(2, l):
  if primes[i]:
    primelist.append(i)
    for j in range(i * 2, l, i):
      primes[j]=False

class Family:
  def __init__(self, member, pattern):
    self.first = member
    self.pattern = pattern
    self.values = [member]
    self.size = 1
  def __lt__(self, other):
    return self.first < other.first
def get_pattern(i):
  pattern=[]
  while i>0:
    pattern.append(i % 2 == 1)
    i//=2
  return pattern

def apply_pattern(pattern, n):
  p_list = list(str(n))
  wildcard_value = None
  for i in range(0, min(len(pattern), len(p_list))):

    if pattern[i]:
      if wildcard_value is None:
        wildcard_value = p_list[i]
      else:
        if wildcard_value != p_list[i]:
          return None
      p_list[i] = '*'

  if wildcard_value is None:
    return None
  return "".join(p_list)

def get_families(pattern, primes, size):
  family_by_pattern={}
  for p in primes:
    p_pattern = apply_pattern(pattern, p)
    if p_pattern is not None:
      if p_pattern in family_by_pattern:
        family_by_pattern[p_pattern].size += 1
        family_by_pattern[p_pattern].values.append(p)
      else:
        family_by_pattern[p_pattern] = Family(p, p_pattern)
  result = []
  for key, family in family_by_pattern.items():
    if family.size == size:
      result.append(family)
  return result

all_families = []
for i in range(1, 2**8):
  pattern=get_pattern(i)
  all_families.extend(get_families(pattern, primelist, 8))
all_families.sort()
print(all_families[0].pattern)
print(all_families[0].values)
print(len(all_families))

