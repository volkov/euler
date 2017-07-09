fivegonmap=[
    [0,1,2],
    [3,2,4],
    [5,4,6],
    [7,6,8],
    [9,8,1]
]
a=[0]*10
used=[False]*10
result=[]
def all():
    res = []
    for i in range(10):
        if not used[i]:
            res.append(i+1)
    return res
def use(i):
    used[i-1]=True
def free(i):
    used[i-1]=False
def is_free(i):
    return 10>=i>0 and not used[i-1]

def fifth(s):
    a[9]=s-a[8]-a[1]
    if is_free(a[9]):
        print(a)
        mini=0
        mina=11
        for i,m in enumerate(fivegonmap):
            if a[m[0]]<mina:
                mini=i
                mina=a[m[0]]
        r=[]
        for z in range(5):
            m=fivegonmap[(z+mini)%5]
            r.append(str(a[m[0]]))
            r.append(str(a[m[1]]))
            r.append(str(a[m[2]]))
        result.append(''.join(r))

def fourth(s):
    for i in all():
        a[7]=i
        use(i)
        a[8]=s-a[7]-a[6]
        if is_free(a[8]):
            use(a[8])
            fifth(s)
            free(a[8])
        free(i)
def third(s):
    for i in all():
        a[5]=i
        use(i)
        a[6]=s-a[4]-a[5]
        if is_free(a[6]):
            use(a[6])
            fourth(s)
            free(a[6])
        free(i)


def second(s):
    for i in all():
        a[3]=i
        use(i)
        a[4]=s-a[3]-a[2]
        if is_free(a[4]):
            use(a[4])
            third(s)
            free(a[4])
        free(i)



for i in all():
    a[0]=i
    use(i)
    for j in all():
        a[1]=j
        use(j)
        for k in all():
            a[2]=k
            use(k)
            second(a[0]+a[1]+a[2])
            free(k)
        free(j)
    free(i)

sres=sorted(filter(lambda s : len(s)==16,result))
print(sres)
print(sres[len(sres)-1])
