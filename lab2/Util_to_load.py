import ObjectSerial
import inspect

serial = ObjectSerial.ObjectSerializer()
serial.form = 'JSON'

serial.load(r'./files/JSON.json')
print(serial.data)
print(serial.data())
