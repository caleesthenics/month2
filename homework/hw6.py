from datetime import datetime as dt
from time import sleep

def checktime(func):
    def wrapper(*args, **kwargs):
        time_now = dt.now()
        print(f'start : {time_now}')
        result = func(*args, **kwargs)
        time_now2 = dt.now()
        print(f'stop : {time_now2}')
        return result
    return wrapper

@checktime
def hello_world():
    print('hello world')
    sleep(2)


hello_world()