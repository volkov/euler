def period(x):
  a=[int(x**0.5)]
  b=[1]
  c=[a[0]]
  indexmap={}
  indexmap[(a[0],b[0],c[0])]=0
  #print("{}, {}/(sqrt({})-{})".format(a[0],b[0],x,c[0]))
  i=0
  while True:
    i+=1
    p=i-1
    a.append(int(b[p]/(x**0.5-c[p])))
    b.append((x-c[p]**2)/b[p])
    c.append(-(b[p]*c[p]-a[i]*x+a[i]*c[p]**2)/b[p])
    #print("{}, {}/(sqrt({})-{})".format(a[i],b[i],x,c[i]))
    t=(a[i],b[i],c[i])
    if t in indexmap:
      print("period for ",x," is ", i-indexmap[t])
      return i-indexmap[t]
    indexmap[t]=i
print(len(list(filter(lambda x: x%2!=0,map(period,filter(lambda x: not (x**0.5).is_integer(),range(2,10001)))))))
