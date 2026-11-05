#functions that return object, memory effiecient
#gen only whn asked for
def myGen():
    for i in range(3):
        yield i
g=myGen()
'''
print(next(g))
print(next(g))
print(next(g))'''
#print(next(g)) the StopIteration
for i in range(3):
    print(next(g))
