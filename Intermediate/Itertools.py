#product: if with lists then the combination of all
from itertools import permutations, count, cycle, islice, repeat
a=[1,2,3]
perm=permutations(a,2)
print(list(perm))
a=['a',4]
for i in islice(cycle(a),9):
    print(i)
for i in repeat(1,5):
    print(i)
