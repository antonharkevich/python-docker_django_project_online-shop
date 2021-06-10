from configparser import SafeConfigParser


config = SafeConfigParser()
config.add_section('main')
config.set('main', 'inf', 'JSON.json')
config.set('main', 'outf', 'Toml.toml')
config.set('main', 'outform', 'Toml')

with open('config.ini', 'w') as f:
    config.write(f)