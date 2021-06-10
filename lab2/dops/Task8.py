from functools import wraps
import time


class RecursiveDict(dict):
    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            self[item] = self.__class__()
            value = self[item]
            return value

def cache(func):
    saved=RecursiveDict()
    @wraps(func)
    def newfunc(*args, **kwargs):
        st=' '.join('{0}{1}'.format(key, val) for key, val in sorted(kwargs.items()))
        if saved[args][st] == {}:
            result = func(*args, **kwargs)
            saved[args][st] = result
            return result
        else:
            print("Cached!")
            return saved[args][st]
    return newfunc

def fib(n):
    if n < 2:
        return 1
    return fib(n-2) + fib(n-1)
            
# start_time = time.time()
# print(fib(20))
# print("--- %s seconds ---" % (time.time() - start_time))

# @cache
# def cfib(n):
#     if n < 2:
#         return 1
#     return cfib(n-2) + cfib(n-1)
            
# start_time = time.time()
# print(cfib(20))
# print("--- %s seconds ---" % (time.time() - start_time))

@cache
def foo(a, b, c):
    return a * b * c

print(foo(2, 4, c=3))
print(foo(2, 4, c=3))
print(foo(b=4, a=2, c=3))
print(foo)