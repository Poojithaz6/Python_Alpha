def start_end_decorator(func):
    def h():
        print("Start")
        func()
        print("End")
    return h
@start_end_decorator
def print_name():
    print('Alex')
#print_name= start_end_decorator(print_name)
print_name()
#without the implemenation
def decorators(func):
    def wrapper(*args,**kwargs):
        print("Start")
        result=func(*args,**kwargs)
        print(result)
        print("End")
        return result
    return wrapper
@decorators
def add5(x):
    return x+5
add5(4)
#with argument