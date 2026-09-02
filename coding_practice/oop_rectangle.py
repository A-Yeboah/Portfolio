# build a Rectangle class with width/height,
# and methods for area() and perimeter()

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        print(f" Area: {self.width * self.height}")

    def perimeter(self):
        print(f"Perimeter: {2*self.width + 2*self.height}")

rectangle = Rectangle(10, 4)
rectangle.area()
rectangle.perimeter()
