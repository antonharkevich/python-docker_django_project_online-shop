import ObjectSerial
import argparse
from configparser import ConfigParser


def main():    
    parser = argparse.ArgumentParser(description='Parser')
    parser.add_argument('inf', type=str, help='Input file')
    parser.add_argument('--outf', type=str, default='', help='Output file')
    parser.add_argument('--outform', type=str, default='', help='Output format')
    args = parser.parse_args() 
    if(args.inf.endswith('.ini')):
        config = ConfigParser()
        config.read(args.inf)
        args.inf = config.get('main', 'inf')
        args.outf = config.get('main', 'outf')
        args.outform = config.get('main', 'outform')

    if((args.inf.endswith('.json')) and (args.outform == 'JSON')):
        pass
    elif((args.inf.endswith('.pickle')) and (args.outform == 'Pickle')):
        pass
    elif ((args.inf.endswith('.yaml')) and (args.outform == 'Yaml')):
        pass
    elif((args.inf.endswith('.toml')) and (args.outform == 'Toml')):
        pass
    else:
        serial = ObjectSerial.ObjectSerializer()
        if(args.inf.endswith('.json')):
            serial.form = 'JSON'
        elif(args.inf.endswith('.pickle')):
            serial.form = 'Pickle'
        elif(args.inf.endswith('.yaml')):
            serial.form = 'Yaml'
        elif(args.inf.endswith('.toml')):
            serial.form = 'Toml'
        serial.load(args.inf, as_dict=1)
        data = serial.data
        serial.change_form(args.outform)
        serial.data = data
        serial.dump(args.outf, as_dict=1)
    
if __name__ == '__main__':
    main()

