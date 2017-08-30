import urllib.request
with urllib.request.urlopen('https://projecteuler.net/project/resources/p081_matrix.txt') as response:
    data = response.read().decode()
m = list(map(lambda line: list(map(int,line.strip().split(','))), data.strip().split('\n')))
print(m)

p = [[0]*len(m[0]) for _ in range(len(m))]
for i in range(len(m)):
    for j in range(len(m[0])):
        minp=0
        if i > 0:
            minp = p[i-1][j]
        if j > 0:
            if i>0:
                minp = min(minp, p[i][j-1])
            else:
                minp = p[i][j-1]
        p[i][j] = minp + m[i][j]
print(p)
print(p[-1][-1])
