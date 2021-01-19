class Circle:

    def __init__(self, radius, pi):
        self.pi = pi
        self.radius = radius

    def circuference(self):
        circumference = 2 * self.pi * self.radius
        print(f"circumference of Circle = {circumference}")

    def diameter(self):
        diameter = 2 * self.radius
        print(f"Dimeter of Circle = {diameter} \n")
