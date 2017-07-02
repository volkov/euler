from functools import reduce
from dsum import dsum
f = reduce(lambda x,y: x*y,range(1,101))
print(dsum(f))
