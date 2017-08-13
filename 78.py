L = 30000 
M = [0]*(L+1)
M0 = [0]*(L+1)
M0[0] = 1
for i in range(1, L+1):
    for j in range(0, L+1):
        for k in range(j, -1, -i):
            M[j] += M0[k]
    if i%100==0:
        print("Processed",i)
    #print(M)
    if M[i]%1000000==0:
        print(i,M[i])
        quit()
    M0=M
    M=[0]*(L+1)
