def solution(D):
    y=1
    while True:
        x=(1+D*y**2)**(0.5)
        if x.is_integer() and x**2-D*y**2==1:
            return (x,y)
        y+=1
maxx=0
maxD=0
for D in range(2,1001):
    if not (D**0.5).is_integer():
        s = solution(D)
        x=s[0]
        if x>maxx:
            maxD=D
            maxx=x
        print("%d^2-%d*%d^2=1"%(x,D,s[1]))
print(maxx)
print(maxD)

