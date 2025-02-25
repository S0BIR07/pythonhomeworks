import math
class Vector:
    def __init__(self, *numbers):
        self.numbers=numbers
    
    def __str__(self):
        return f"Vector{self.numbers}"
    
    def __len__(self):
        return len(self.numbers)
    
    def __add__(self, other):
        if len(self)!=len(other):
            raise ValueError("Two vectors are not of the same dimention!")
        return Vector(*(a+b for a,b in zip(self.numbers, other.numbers)))
    
    def __sub__(self, other):
        if len(self)!=len(other):
            raise ValueError("'Two vectors are not of the same dimension!")
        return Vector(*(a-b for a,b in zip(self.numbers,other.numbers)))
    
    def __mul__(self, other):
        if len(self)!=len(other):
            raise ValueError("Two vectors are not of the same dimention!")
        return sum((a*b for a,b in zip(self.numbers,other.numbers)))
    
    def __rmul__(self, num:int):
        return Vector(*(a*num for a in self.numbers))
    
    def magnitude(self):
        return math.sqrt(sum(a**2 for a in self.numbers))

    def normalize(self):
        if self.magnitude()==0:
            raise ValueError("Vector with 0 magnitude cannot be normalized!")
        return Vector(*(round(a/self.magnitude(),3) for a in self.numbers)) 
    
vec1 = Vector(1,2,5,4,6)
vec2 = Vector(2,1,4,1,1)
vec3 = vec2-vec1
vec4 = vec1 + vec2
vec5 = 3*vec1
dot_product = vec1*vec2
magnitude = vec2.magnitude()
normalize = vec1.normalize()
print(vec3)
print(vec4)
print(vec5)
print(dot_product)
print(magnitude)
print(normalize)