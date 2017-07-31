pp = set()
for i in range(1, 5001):
    for j in range(i, 5001):
        p = i * j
        li = list(str(i))
        lj = list(str(j))
        lp = list(str(p))
        if len(li) + len(lj) + len(lp) == 9:
            s = set(li + lj + lp)
            if len(s) == 9 and '0' not in s:
                print("{}*{}={}".format(i, j, p))
                pp.add(p)
print(sum(pp))
