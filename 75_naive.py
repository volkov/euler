from math import ceil
L = 1000
n = 0
values = [[] for i in range(L + 1)]
for c in range(1, (L + 1) // 2):
    cc = c**2
    print("checking for {} as {}...........".format(c,cc))
    i = 1
    j = int((cc - i**2)**0.5)
    i_step = True
    while i < j and i + j + c <= L:
        ii=i**2
        jj=j**2
        print("      {}^2+{}^2={}".format(i,j,ii+jj))
        if ii + jj == cc:
            print("  passed",i,j)
            values[i + j + c].append((i, j, c))
            if i_step:
                i += 1
            else:
                j -= 1
        else:
            if i_step:
                i = ceil((cc - jj)**0.5)
            else:
                j = int((cc - ii)**0.5)
        i_step = not i_step

print(len(list(filter(lambda v: len(v)==1,values))))
#for i, v in enumerate(values):
#    if len(v):
#        print(i, v)
