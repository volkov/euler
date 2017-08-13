L = 1500000
n = 0
values = [set() for i in range(L + 1)]
for m in range(1, int(L**0.5) + 1):
    for n in range(1, m):
        a = m**2 - n**2
        b = 2 * m * n
        if a > b:
            a, b = b, a
        c = m**2 + n**2
        if a**2 + b**2 == c**2:
            k = 1
            while (a * k + b * k + c * k < L):
                values[a * k + b * k + c * k].add((a * k, b * k, c * k))
                k += 1
print(len(list(filter(lambda v: len(v) == 1, values))))
#for i, v in enumerate(values):
#    if len(v):
#        print(i, v)
