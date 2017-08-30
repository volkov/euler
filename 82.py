import urllib.request
with urllib.request.urlopen('https://projecteuler.net/project/resources/p082_matrix.txt') as response:
    data = response.read().decode()
m = list(map(lambda line: list(map(int, line.strip().split(','))),
             data.strip().split('\n')))
print(m)
N = len(m)
p = [[-1] * N for _ in range(N)]
r = set()
for i in range(N):
    p[i][0] = m[i][0]
    r.add((i, 1))
while len(r):
    minlen = float('inf')
    for x, y in r:
        if p[x][y-1]>=0:
            clen = p[x][y - 1] + m[x][y]
            if minlen > clen:
                minlen = clen
                minxy = (x, y)
        if x > 0 and p[x - 1][y] >= 0:
            clen = p[x - 1][y] + m[x][y]
            if minlen > clen:
                minlen = clen
                minxy = (x, y)
        if x < N - 1 and p[x + 1][y] >= 0:
            clen = p[x + 1][y] + m[x][y]
            if minlen > clen:
                minlen = clen
                minxy = (x, y)
    x, y = minxy
    p[x][y] = minlen
    r.remove((x,y))
    if x > 0 and p[x - 1][y] < 0:
        r.add((x - 1, y))
    if x < N - 1 and p[x + 1][y] < 0:
        r.add((x + 1, y))
    if y < N - 1 and p[x][y + 1] < 0:
        r.add((x, y + 1))

print(p)
print(list(map(lambda x: x[-1], p)))
print(min(map(lambda x: x[-1], p)))
