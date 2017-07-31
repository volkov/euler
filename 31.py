L=200
coin_list=[1,2,5,10,20,50,100,200]
m=[[0]*(L+1) for _ in range(len(coin_list))]
m[0][0]=1
for i,c in enumerate(coin_list):
    for j in range(L+1):
        if i==0:
            m[i][j]=1
        else:
            for k in range(j,-1,-c):
                m[i][j]+=m[i-1][k]
    print(m[i])
