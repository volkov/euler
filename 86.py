L = 2000
n = 0
values = set()
for m in range(1, int((L*2)**0.5) + 1):
    for n in range(1, m):
        a = m**2 - n**2
        b = 2 * m * n
        if a > b:
            a, b = b, a
        c = m**2 + n**2
        if a**2 + b**2 == c**2:
            k = 1
            while (b * k <= L * 2):
                values.add((a * k, b * k, c * k))
                k += 1
cubes = [set() for _ in range(L+1)]
for a, b, c in values:
    for i in range(1, a):
        x = a - i
        z = i
        y = b
        if c <= ((y + z)**2 + x**2)**0.5 and c <= ((x + y)**2 + z**2)**0.5 and x <= L and y <= L and z <= L:
            cubes[max(x,y,z)].add(tuple(sorted([y, x, z])))
    for i in range(1, b):
        x = b - i
        z = i
        y = a
        if c <= ((y + z)**2 + x**2)**0.5 and c <= ((x + y)**2 + z**2)**0.5 and x <= L and y <= L and z <= L:
            cubes[max(x,y,z)].add(tuple(sorted([x, y, z])))

s = 0
for i, c in enumerate(cubes):
    s+=len(c)
    if s >= 10**6:
        print(i,s)
        quit()
print(s)

print(len(cubes))

