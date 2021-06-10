class RecursiveDict(dict):
    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            self[item] = self.__class__()
            value = self[item]
            return value

a = RecursiveDict()
a[1][2][3] = 4
a[1][2][4]=5
a[1][1][5]=10
a[2][1][5] = 15
print(a[54][5][54])
a[54][2]=2
a['a']['b']=1
print(a)




