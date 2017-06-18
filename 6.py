r = range(1,101)
print sum(r)**2 - reduce(lambda x,y:x+y,map(lambda x: x**2, r))
