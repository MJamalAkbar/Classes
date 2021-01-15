class Quadrant:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        area2 = self.length * self.width
        print(f"Area of rectangle = {area2}")

        area2 = self.length * self.length
        print(f"Area of Square = {area2}")

    def perimerter(self):
        perimeter1 = 2 * (self.length + self.width)
        print(f"Perimeter of Rectangle = {perimeter1}")

        perimeter2= 4 * self.length
        print(f"Perimeter of square = {perimeter2}")

class Circle:
    def __init__(self, radius, pi):
        self.radius = radius
        self.pi = pi

    def area(self):
        Area = self.pi * self.radius * self.radius
        print(f"Area of the circle = {Area}")

    def circumference(self):
        Circumferance = 2 * (self.pi * self.radius)
        print(f"Circumference f a circle => {Circumferance}")

    def Diameter(self):
        Diameter = 2 * self.radius
        print(f"Area of the Diameter = {Diameter}")

object_Quad = Quadrant(length=4, width=12)
object_Quad.area()
object_Quad.perimerter()

object_Circle = Circle(radius=1.4, pi=3.14)
object_Circle.area()
object_Circle.circumference()
object_Circle.Diameter()