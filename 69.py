import primes

def is_perm(x,y):
    return sorted(list(str(x)))==sorted(list(str(y)))

L=10**6
prime = primes.primes(L)
print(len(prime),"primes")
prime_normal = [0]*len(prime)
phi_parts = [1]*len(prime)
phi = [0]*L
number=1
phi_number=1
i=0
to_drop=0
pos_stack=[]
while True:
    new_number = number*prime[i]
    if new_number<L:
        if prime_normal[i]>0:
            phi_multiplier=prime[i]
        else:
            phi_multiplier=prime[i]-1
        prime_normal[i]+=1
        phi_parts[i]*=phi_multiplier
        phi_number*=phi_multiplier
        number = new_number
        #assert phi[number]==0
        phi[number]=phi_number
        if len(pos_stack)>0 and pos_stack[-1]<i:
            print("unexpected i", i)
            print("stack ",pos_stack)
            print(prime_normal)
            print(prime)
        if len(pos_stack)==0 or pos_stack[-1]!=i:
            #print("append",i)
            pos_stack.append(i)
        #print("phi({})={}".format(number,phi_number))
        i=0
    else:
        #print("drop from ",i)
        #for j in range(i,-1,-1):
        if prime_normal[i]>0:
            number//=prime[i]**prime_normal[i]
            phi_number//=phi_parts[i]
            prime_normal[i]=0
            phi_parts[i]=1
            #print(pos_stack)
            #print(prime_normal)
            #print(prime)
            #print("pop")
            pos_stack.pop()
            i+=1
        elif len(pos_stack)>0:
            i=pos_stack[-1]
        else:
            i+=1
        if i==len(prime):
            break;
#for i,p in enumerate(phi):
#  print("phi({})={}".format(i,p))

maxratio = 0
mixi = 0
for i in range(2,L):
    p = phi[i]
    ratio = i/p
    if ratio>maxratio:
        maxratio = ratio
        maxi=i
print(maxratio)
print(maxi)
