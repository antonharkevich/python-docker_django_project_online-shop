class Vector:
    def __init__(self, components):
        self.components = components # components should be a list 

    def add(self, other):
        added_components = []
        if len(other.components) == len(self.components):
            for i in range(len(self.components)):
                added_components.append(self.components[i] + other.components[i])
            return Vector(added_components)
        else:
            print("Dimensions isn't equal, we return empty vector")
            return Vector(added_components)
        
    
    def sub(self, other):
        subed_components = []
        if len(other.components) == len(self.components):
            for i in range(len(self.components)):
                subed_components.append(self.components[i] - other.components[i])
            return Vector(subed_components)
        else:
            print("Dimensions isn't equal, we return empty vector")
            return Vector(subed_components)
        
    def mul(self, scalar):
        new_components = []
        for i in range(len(self.components)):
            new_components.append(self.components[i] * scalar)
        return Vector(new_components)
    
    def scalar_mul(self, other):
        result = 0
        if len(other.components) == len(self.components):
            for i in range(len(self.components)):
                result += self.components[i] * other.components[i]
            return result
        else:
            print("Dimensions isn't equal, we return zero")
            return result
            
    def dimensions(self):
        return len(self.components)
        
    def index(self, i):
        return self.components[i]
    
    def length(self):
        norm=0
        for i in range(len(self.components)):
            norm+=self.components[1] ** 2
        return norm ** (1/2)
            
    def to_string(self):
        return '(' + (', '.join(str(e) for e in self.components)) + ')'    
    
    def equal(self, other):
        return self.to_string() == other.to_string()

vect1 = Vector([1, 2, 3])
print(vect1.equal(Vector([1,2,3]))    
       