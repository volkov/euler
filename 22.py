from urllib.request import urlopen
with urlopen('https://projecteuler.net/project/resources/p022_names.txt') as f:
  names = sorted(list(map(lambda s:s[1:-1],f.read().decode().split(','))))
print(names)
def score(s):
  return sum(map(lambda c: ord(c)-ord('A')+1,list(s)))
result=0
for i,n in enumerate(names):
  result+=score(n)*(i+1)
print(result)
