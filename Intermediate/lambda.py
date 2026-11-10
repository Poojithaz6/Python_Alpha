#sorted
a=[(1,2),(4,-1),(8,7),(-9,10)]
a_sort=sorted(a,key=lambda x:x[1])
print(a)
print(a_sort)

#expression
#map : map(func,seq)
a=[1,2,3,4]
b=list(map(lambda x:x**2,a))
print(b)
#filter: filter(func,seq) returns for which the func is true
#reduce : reduce(func,seq) gotta import from functools
from functools import reduce
prod=reduce(lambda x,y:x*y,a)
print(prod)