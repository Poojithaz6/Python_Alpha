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