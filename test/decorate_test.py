from functools import wraps  # functools 모듈로부터 wraps 데코레이터를 가져온다.


def decorator2(func):
    @wraps(func)  # wrapper2에 붙여준다.
    # wraps를 안해주면, 두 함수를 불렀을때, Decorator2가 decorator1을 데코해주세되어서 fuction이 함수로 들어오지 않고 warapper1이 함수로 들어오게 됨
    def wrapper2(*args, **kwargs):
        print(f'{func.__name__} has been decorated again by decorator2')
        return func(*args, **kwargs)
    return wrapper2


def decorator1(func):
    @wraps(func)  # wrapper1에 붙여준다.
    def wrapper1(*args, **kwargs):
        print(f'{func.__name__} has been decorated by decorator1')
        return func(*args, **kwargs)
    return wrapper1

@decorator2
@decorator1
def function():
    print(f'This is original function')

function()