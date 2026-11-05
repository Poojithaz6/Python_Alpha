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
greet()'''
import time
def timeControl(func):
    def wrapper(*args,**kwargs):
        start_time=time.time()
        func(*args,**kwargs)
        end_time=time.time()
        return end_time-start_time
    return wrapper
@timeControl
def add(a,b):
    time.sleep(2)
    return a+b
print(add(3,4))