import inspect
import datetime

def logit(method, name):
    def timed(*args, **kwargs):
        result = method(*args, **kwargs)
        now = datetime.datetime.now()
        my_file = open(f"{name}.txt", "w")
        my_file.write(f' {now}\n')
        my_file.write(f' Вызван метод с именем: {method.__name__} у класса с именем: {name}\n')
        my_file.write(f' Его аргументы: {args, kwargs}\n')
        my_file.write(f' Его резлультат: {result}\n\n')
        my_file.close()
        return result
    return timed

class Logger(object):
    def __getattribute__(self, s):
        attr = super(Logger, self).__getattribute__(s)
        if inspect.ismethod(attr): 
            return logit(attr, self.__class__.__name__)
        else:
            return attr

    def simple(self, a, b):
        return a*b

    def __str__(self):
        my_file = open(f"{self.__class__.__name__}.txt", "r")
        my_string = my_file.read()
        my_file.close()
        return my_string

class Simple_class(Logger):
    def simple_function(self, a, b):
        return a*b

x=Logger()
x.simple(2, 3)
res=Simple_class()
res.simple_function(1, 2)
print(res)
print(x)