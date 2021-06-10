from setuptools import setup
from os.path import join, dirname

setup(
    name='new_custom_parser',
    version='1.0',
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
    py_modules=["console_util", "ObjectSerial", "SerializerFactory","JSONSerializer","TomlSerializer","YamlSerializer","PickleSerializer"],
    entry_points={
        'console_scripts': [
            'new_custom_parser = console_util:main',
        ],
    }
)





