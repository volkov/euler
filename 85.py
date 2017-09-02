import itertools

L=2*10**6

def count_rectangles(m,n):
    res = 0
    for i in range(m):
        for j in range(n):
            res+=(m-i)*(n-j)
    return res

mindiff = 10**6

for i in itertools.count(1):
    for j in itertools.count(1):
        c = count_rectangles(i,j)
        if abs(c-L)<mindiff:
            mindiff = abs(c-L)
            minvalue = (i,j)
        if (c>L):
            break
    if j==1:
        break


print(mindiff)
print(minvalue)
