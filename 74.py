from math import factorial
from dsum import digits

N = 10**6
c = 0
for i in range(1, N + 1):
    chain = set()
    while i not in chain:
        chain.add(i)
        i = sum(map(factorial, digits(i)))
    # print(chain)
    if len(chain) == 60:
        c += 1
print(c)
