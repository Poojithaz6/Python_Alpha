from timeit import default_timer as timer

my_list=['a']*100000
print(my_list)
def decorator(func):
    def wrapper(*args,**kwargs):
        start=timer()
        result=func(*args,**kwargs)
        end=timer()
        return (end-start)
    return wrapper
@decorator
def by_join(x):
    new_str = ' '.join(x)
    print(new_str)
@decorator
def withuou_join(x):
    my_string = ''
    for i in x:
        my_string += i
    print(my_string)
#without join
print(by_join(my_list))
print(withuou_join(my_list))
