import SerializerFactory
import inspect
import io
import builtins
import base64
import types
import pickle
from pickle import Pickler, Unpickler


class ObjectSerializer:
    def __init__(self):
        self.string = None
        self.data = None
        self.form = None

    def change_form(self, new_form):
        if self.form == new_form:
            return False
        else:
            self.string = None
            self.data = None
            self.form = new_form
            return True

    def save_function(self, obj):
        code_keys = [
            "argcount", "posonlyargcount", "kwonlyargcount", 
            "nlocals", "stacksize", "flags", "code", "consts",
            "names", "varnames", "filename", "name", "firstlineno",
            "lnotab", "freevars", "cellvars"
        ]
        code_values = [getattr(obj.__code__, 'co_' + key) for key in code_keys]
        code = dict(zip(code_keys, code_values))
        func_keys = [
            "globals", "name", "defaults", 
            "closure", "dict", "kwdefaults"
        ]
        func_values = [getattr(obj, f'__{key}__') for key in func_keys]
        func = dict(zip(func_keys, func_values))
        fglobals = {key: self.decode_to_dict(value) for key, value 
            in func['globals'].items() if key in code['names']}
        func.update({'globals': fglobals})
        func_dict = {'CodeType': code, 'FunctionType': func} 
        return func_dict

    def decode_to_dict(self, obj):
        name = None
        try:
            name = obj.__name__
        except:
            pass
        base_class = None
        try:
            base = obj.__base__
            if base is not object: 
                base_class = self.decode_to_dict(base)
            else:
                base_class = ()
        except:
            pass
        class_attrs = None
        base_types = (int, float, bool, str, list, tuple, dict, set)
        if isinstance(obj, (*base_types, types.FunctionType, types.MethodType)):
            pass
        try: 
            all_attr = {**{key: value for key, value in inspect.getmembers(obj, 
                        predicate=inspect.isfunction)}, 
                        **{key: value for key, value in inspect.getmembers(obj) 
                        if not (key.startswith('__') and key.endswith('__'))}}
            for key, value in all_attr.items():
                if not isinstance(value, base_types):
                    all_attr[key] = self.decode_to_dict(value)
            class_attrs = all_attr
        except AttributeError:
            pass
        func_args = None
        try:
            full_args = inspect.getfullargspec(obj)
            args_spec = (full_args.args, full_args.varargs, full_args.varkw, 
                        full_args.defaults, full_args.kwonlyargs, 
                        full_args.kwonlydefaults, full_args.annotations)
            func_args = dict(zip(full_args._fields, args_spec))
        except:
            pass
        our_obj = obj
        if isinstance(obj, (types.FunctionType, types.MethodType)):
            our_obj = self.save_function(obj)
        res = None
        res1 = None
        try:
            f = io.BytesIO()
            pickle.dump(our_obj, file=f, protocol=None, fix_imports=True, buffer_callback=None)
            res = f.getvalue()
            res1 = base64.b85encode(res).decode('ascii')
        except TypeError:
            pass
        template = {
            'representation': repr(obj),
            'name': name,
            'type': str(type(obj)).split('\'')[1],
            'base': base_class,
            'class_attr': class_attrs,
            'func_param': func_args,
            'object': res1
        }
        return {key : value for key, value in template.items() if value}
    
    def encode(self, obj_dict):
        if not isinstance(obj_dict, dict): 
            return obj_dict
        elif obj_dict.get('type', None) in ('function', 'method'):
            try:
                dec_obj = obj_dict.get('object', None)
                dec_obj = base64.b85decode(dec_obj.encode('ascii'))
                f = io.BytesIO(dec_obj)
                if isinstance(dec_obj, str):
                        raise TypeError("Can't load pickle from unicode string")
                data = pickle.load(file=f, encoding="ASCII", fix_imports=True, errors="strict", buffers=None)
                for key, value in data['FunctionType']['globals'].items():
                    data['FunctionType']['globals'][key] = self.encode(value)
                data['FunctionType']['globals'].update({'__builtins__': builtins})
                func_code = types.CodeType(*data['CodeType'].values())
                func_params = list(data['FunctionType'].values())
                func = types.FunctionType(func_code, *func_params[:-2])
                func.__dict__.update(func_params[4]) 
                if func_params[5] is not None:
                    func.__kwdefaults__ = func.__kwdefaults__
                return func
            except:
                return None
        else:
            try:
                dec_obj = obj_dict.get('object', None)
                dec_obj = base64.b85decode(dec_obj.encode('ascii'))
                f = io.BytesIO(dec_obj)
                if isinstance(dec_obj, str):
                        raise TypeError("Can't load pickle from unicode string")
                data = pickle.load(file=f, encoding="ASCII", fix_imports=True, errors="strict", buffers=None)
                return data
            except:
                class_name = obj_dict.get('name', 'SomeClass')
                class_attr = obj_dict.get('class_attr', {})
                for key, value in class_attr.items():
                    class_attr[key] = self.encode(value)
                base_class = self.encode(obj_dict.get('base_class', ()))
                new_class = type(class_name, base_class, class_attr)
                if obj_dict.get('name', None):
                    return new_class
                else:
                    return new_class()

    def load(self, fp, as_dict=0):
        serializer = SerializerFactory.factory.get_serializer(self.form)
        self.data = serializer.load(fp)
        if as_dict == 0:
            self.data = self.encode(self.data)
    
    def loads(self, as_dict=0):
        serializer = SerializerFactory.factory.get_serializer(self.form)
        self.data = serializer.loads(self.string)
        if as_dict == 0:
            self.data = self.encode(self.data)
    
    def dump(self, fp, as_dict=0):
        serializer = SerializerFactory.factory.get_serializer(self.form)
        if as_dict == 0:
            serializer.dump(self.decode_to_dict(self.data), fp)
        else:
            serializer.dump((self.data), fp)

    def dumps(self, as_dict=0):
        serializer = SerializerFactory.factory.get_serializer(self.form)
        if as_dict == 0:
            self.string = serializer.dumps(self.decode_to_dict(self.data))
        else:
            self.string = serializer.dumps((self.data))