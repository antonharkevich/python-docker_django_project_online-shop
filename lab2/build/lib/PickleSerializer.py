import pickle


class PickleSerializer:
    def load(self, fp):
        data = pickle.load(open(fp, "rb"))
        return data


    def loads(self,s):
        data = pickle.loads(s)
        return data
        
    def dumps(self, obj):
        str = pickle.dumps(obj)
        return str
            
    def dump(self, obj, fp):
        pickle.dump(obj, open(fp, "wb"))
