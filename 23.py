from divisors import proper_divisors
def abudant(n):
    return sum(proper_divisors(n))>n
L=30000
a=[False]*L
s=0
for i in range(1,L):
    if abudant(i):
        a[i]=True
    is_sum = False
    for j in range(1,i):
        if a[j] and a[i-j]:
            is_sum=True
            break
    if not is_sum:
        print(i)
        s+=i
print(s)
