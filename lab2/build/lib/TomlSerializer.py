import toml


class TomlSerializer:
    def load(self, fp):
        with open(fp, 'r') as f:
            data = toml.load(f)
        return data       

    def loads(self,s):
        data = toml.loads(s)
        return data
    
    def dumps(self, obj):
        str = toml.dumps(obj)
        return str
                
    def dump(self, obj, fp):
        with open(fp, 'w') as f:
            toml.dump(obj, f)
    