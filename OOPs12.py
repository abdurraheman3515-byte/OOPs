

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False


p1 = Point(10, 20)
p2 = Point(15, 20)

if p1 == p2:
    print("Pass")
else:
    print("Fail")

