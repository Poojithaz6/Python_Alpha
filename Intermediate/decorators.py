'''def start_end_decorator(func):
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
def repeat(n):
    def decorator(func):
        def wrapper(*args,**kwargs):
            for i in range(n):
                func(*args,**kwargs)
        return wrapper
    return decorator

@repeat(n=7)#gotta give the input in the decorstor call and it takes a new fn along with wrapper so that the times variable can be taken into consideration.
def greet():
    print("Hello Poojitha")
greet()
import time
import functools
from doctest import debug


def timeControl(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        start_time=time.time()
        result=func(*args,**kwargs)
        end_time=time.time()
        print("time take:",end_time-start_time)
        return result
    return wrapper
@timeControl
def add(a,b):
    time.sleep(2)
    return a+b
print(add(3,4))
#if multiple decorators then in the order of @
'''
#class decorators :: maintain and update a state
class countCalls:
    def __init__(self,func):
        self.func=func
        self.num_calls=0
    def __call__(self, *args, **kwargs):
        self.num_calls+=1
        print(f'This is  executed {self.num_calls} times')
        return self.func(*args,**kwargs)
@countCalls
def say_helo():
    print('Hello')
say_helo()
say_helo()