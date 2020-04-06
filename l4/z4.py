import math
from inspect import getfullargspec
from collections import defaultdict


class overload:
    funcs = defaultdict(dict)

    def __init__(self, func):
        self.funcs = overload.funcs[func.__name__]
        args_count = len(getfullargspec(func).args)
        self.funcs[args_count] = func

    def __call__(self, *args, **kwargs):
        return self.funcs[len(args)](*args, **kwargs)



@overload
def norm(x, y):
    return math.sqrt(x*x + y*y)


@overload
def norm(x, y, z):
    return abs(x) + abs(y) + abs(z)


@overload
def notnorm(x, y):
    return 1


print(norm(2, 4))
print(norm(2, 3, 4))
print(notnorm(2, 4))
