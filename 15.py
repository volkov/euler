N = 21
m = [[0] * N for _ in range(N)]
m[0][0] = 1
for i in range(N):
  for j in range(N):
    if i > 0:
      m[i][j] += m[i - 1][j]
    if j > 0:
      m[i][j] += m[i][j - 1]
for k in m: print(k)
print(m[N - 1][N - 1])
