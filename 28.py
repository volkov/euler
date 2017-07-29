step=0
n=1
s=1
L = 1001 
print(n)
while n < L*L:
    step+=2
    for i in range(4):
        n+=step
        print(n)
        s+=n
print(s)

