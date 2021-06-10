import json



class JSONSerializer:
    def load(self, fp):
        f = open(fp) 
        data = json.load(f) 
        f.close() 
        return data

    def loads(self,s):
        data = json.loads(s)
        return data
    
    def dumps(self, obj):
        str = json.dumps(obj)
        return str
            
    def dump(self, obj, fp):
        json.dump(obj, open(fp,"w"))