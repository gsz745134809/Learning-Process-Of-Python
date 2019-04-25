# 装饰器是一种非常有用的设计模式

# 简单装饰器
from functools import wraps
def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("wrap function")
        return func(*args, **kwargs)
    return wrapper

@decorator
def example(*a, **kw):
    pass

example.__name__  # attr of function preserve
# 'example'
# Decorator


# 带输入值的装饰器

from functools import wraps
def decorator_with_argument(val):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("Val is {0}".format(val))
            return func(*args, **kwargs)
        return wrapper
    return decorator

@decorator_with_argument(10)
def example():
    print("This is example function.")

example()
# Val is 10
# This is example function.

# 等价于

def example():
    print("This is example function.")

example = decorator_with_argument(10)(example)
example()
# Val is 10
# This is example function.
