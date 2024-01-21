import time
import logging

def log(func):
    def wrapper(*args,**kwargs):
        print("start time"+str(time.time())+str(args[0]))

        func(args[0],args[1])

        print("end time"+str(time.time())+str(args[0]))
    return wrapper

@log
def  add(a,b):
    print(a+b)

res = add(2,3)
        
print(res)