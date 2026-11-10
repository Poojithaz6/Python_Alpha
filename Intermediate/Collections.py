# counter
from collections import Counter, OrderedDict

my_str="aabbbgggdd"
my_counter=Counter(my_str)
print(my_counter)

#namedTuple
from collections import namedtuple
Point=namedtuple('Point','x,y')
pt=Point(1,4)
pt2=Point(8,7)
print(pt2)

#OrderedDict: just to remember the order of adding key value
#defaultdict: if there are no value nd key then return default value

#defaultdict(int or list or ect)
#deque : appendleft or extedleft
from collections import deque
d=deque()
d.append(1)
d.append(2)
d.extendleft([4,5,6])
d.rotate()
print(d)
