import ObjectSerial
import inspect
from Util_to_load import some_function

a = 54

def simple_function():
    return some_function(4) + 1

class simple_class:
    attr1 = 4
    attr2 = [1, 2, 3, 4, 5]

    def __str__(self):
        return str(self.attr1)

class very_big_class(simple_class):
    attr3 = [1, 2, 3, 4, 4, 5]
    def __init__(self, obj1):
        self.attr4 = obj1

    def some_function(self, x):
        return self.attr4 * x * 2

serial = ObjectSerial.ObjectSerializer()
serial.form = 'Yaml'

x = simple_class()
serial.change_form('JSON')
serial.data = simple_function
serial.dump(r'./files/JSON.json')



