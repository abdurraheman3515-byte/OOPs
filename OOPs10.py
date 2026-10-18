import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Square:
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2

C = Circle(5)
print(C.area())

S = Square(5)
print(S.area())