import yaml


class YamlSerializer:
    def load(self, fp):
        data = yaml.load(open(fp, "rb"))
        return data


    def loads(self,s):
        data = yaml.load(s)
        return data

    
    def dumps(self, obj):
        str = yaml.dump(obj)
        return str

    def dump(self, obj, fp):
        yaml.dump(obj, open(fp, "w"))