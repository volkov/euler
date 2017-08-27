import urllib.request
with urllib.request.urlopen('https://projecteuler.net/project/resources/p079_keylog.txt') as response:
    data = response.read().decode()
greater=[set() for _ in range(10)]
smaller=[set() for _ in range(10)]
for line in data.split('\n'):
    if len(line)>0:
        print("line",line)
        l0 = int(line[0])
        l1 = int(line[1])
        l2 = int(line[2])
        greater[l0].add(l1)
        greater[l0].add(l0)
        greater[l0].add(l2)
        greater[l1].add(l1)
        greater[l1].add(l2)
        greater[l2].add(l2)
res=[]
for i,v in enumerate(greater):
    print(i,v)
    if len(v)>0:
        res.append((i,v))
res_sorted = sorted(res,key=lambda x: len(x[1]))
print(res_sorted)
