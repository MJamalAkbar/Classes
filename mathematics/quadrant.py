class Quadrant:
    def __init__(self, length, width=None):
        self.length = length
        self.width = width

    def area(self):
        if self.length and self.width is None:
            area2 = self.length * self.length
            print(f"Area of Square (New) = {area2} ")
        else:
            area2 = self.length * self.width
            print(f"Area of rectangle (New) = {area2} ")

    def perimerter(self):
        if self.length and self.width is None:
            perimeter2 = 4 * self.length
            print(f"Perimeter of square  = {perimeter2} \n")


        else:
            perimeter1 = 2 * (self.length + self.width)
            print(f"Perimeter of Rectangle = {perimeter1} \n")
