class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

Point1 = Point(1, 2)
Point2 = Point(4, 6)

print(Point1.distance(Point2))

print(Point1) 

if (Point1 == Point2):
    print("Points are equal")
else:
    print("Points are not equal")  # Output: Points are not equal


class Vector(Point):

    def __init__(self, x, y):
        super().__init__(x,y)

    def magnitude(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

Vector1 = Vector(1,2)
Vector2 = Vector(3,4)
Vector3 = Vector1+Vector2

print(Vector3)
print(Vector3.distance(Vector3))