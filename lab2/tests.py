import unittest
import ObjectSerial
import SerializerFactory
import JSONSerializer
import TomlSerializer
import YamlSerializer
import PickleSerializer


a = 54

def simple_function():
    return a+1

class simple_class:
    attr1 = 4
    attr2 = [1, 2, 3, 4, 5]

class big_class(simple_class):
    attr3 = [1, 2, 3, 4, 4, 5]
    def __init__(self, obj1):
        self.attr4 = obj1

    def some_function(self, x):
        return self.attr4 * x

class SerialTestCase(unittest.TestCase):
    def setUp(self):
        self.serial = ObjectSerial.ObjectSerializer()
        self.factory = SerializerFactory.SerializerFactory()
    
    def test_SerializerFactory_create(self):
        self.factory.create_serializer('JSON', JSONSerializer.JSONSerializer)
        self.assertEqual(self.factory._creators['JSON'], JSONSerializer.JSONSerializer, 'incorrect create function in SerializerFactory')

    def test_SerializerFactory_get(self):
        self.factory.create_serializer('JSON', JSONSerializer.JSONSerializer)
        serial = self.factory.get_serializer('JSON')
        self.assertEqual(isinstance(serial,JSONSerializer.JSONSerializer), True, 'incorrect get function in SerializerFactory')

    def test_ObjectSerializer_change_form(self):
        self.serial.change_form('JSON')
        self.assertEqual(self.serial.form, 'JSON', 'incorrect change_form function')
        self.assertEqual(self.serial.change_form('JSON'), False, 'incorrect change_form function in ObjectSerializer')

    def test_JSON_Serializer(self):
        self.serial.change_form('JSON')
        self.serial.data = big_class(54)
        self.serial.dump(r'./files/JSON.json')
        handle = open(r'./files/JSON.json', "r")
        data = handle.read()
        handle.close()
        self.serial.dumps()
        self.assertEqual(self.serial.string, data, 'incorrect JSON dumps and dump functions')
        self.serial.load(r'./files/JSON.json')
        self.assertEqual(self.serial.data.some_function(2), 108, 'incorrect JSON load function')
        self.serial.loads()
        self.assertEqual(self.serial.data.some_function(2), 108, 'incorrect JSON loads function')
    
    def test_Toml_Serializer(self):
        self.serial.change_form('Toml')
        self.serial.data = simple_function
        self.serial.dump(r'./files/Toml.toml')
        handle = open(r'./files/Toml.toml', "r")
        data = handle.read()
        handle.close()
        self.serial.dumps()
        self.assertEqual(self.serial.string, data, 'incorrect Toml dumps and dump functions')
        self.serial.load(r'./files/Toml.toml')
        self.assertEqual(self.serial.data(), 55, 'incorrect Toml load function')
        self.serial.loads()
        self.assertEqual(self.serial.data(), 55, 'incorrect Toml loads function')

    def test_Yaml_Serializer(self):
        self.serial.change_form('Yaml')
        self.serial.data = simple_function
        self.serial.dump(r'./files/Yaml.yaml')
        handle = open(r'./files/Yaml.yaml', "r")
        data = handle.read()
        handle.close()
        self.serial.dumps()
        self.assertEqual(self.serial.string, data, 'incorrect Yaml dumps and dump functions')
        self.serial.load(r'./files/Yaml1.yaml')
        self.assertEqual(self.serial.data.some_function(2), 216, 'incorrect Yaml load function')
        self.serial.load(r'./files/Yaml1.yaml', as_dict=1)
        self.serial.dumps(as_dict=1)
        self.serial.loads()
        self.assertEqual(self.serial.data.some_function(2), 216, 'incorrect Yaml loads function')

    def test_Pickle_Serializer(self):
        self.serial.change_form('Pickle')
        self.serial.data = [1, 2, 3, 4, 5]
        self.serial.dump(r'./files/Pickle.pickle')
        handle = open(r'./files/Pickle.pickle', "rb")
        data = handle.read()
        handle.close()
        self.serial.dumps()
        self.assertEqual(self.serial.string, data, 'incorrect Pickle dumps and dump functions')
        self.serial.load(r'./files/Pickle.pickle')
        self.assertEqual(self.serial.data[1], 2, 'incorrect Pickle load function')
        self.serial.loads()
        self.assertEqual(self.serial.data[2], 3, 'incorrect Pickle loads function')

if __name__ == '__main__':
    unittest.main()