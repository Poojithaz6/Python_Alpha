#product: if with lists then the combination of all
from itertools import permutations, count, cycle, islice
a=[1,2,3]
perm=permutations(a,2)
print(list(perm))
a=['a',4]
for i in islice(cycle(a),9):
    print(i)
