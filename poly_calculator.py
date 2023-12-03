class Rectangle:
    # Constructor: Initializes a new instance of the Rectangle class with width and height.
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Method to set the width of the rectangle.
    def set_width(self, width):
        self.width = width

    # Method to set the height of the rectangle.
    def set_height(self, height):
        self.height = height

    # Method to calculate the area of the rectangle.
    def get_area(self):
        return self.width * self.height

    # Method to calculate the perimeter of the rectangle.
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    # Method to calculate the diagonal of the rectangle.
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    # Method to return a string that visually represents the rectangle using asterisks (*).
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        return ("*" * self.width + "\n") * self.height

    # Method to calculate how many times a given shape can fit inside the rectangle.
    def get_amount_inside(self, shape):
        return self.get_area() // shape.get_area()

    # Special method to define the string representation of the Rectangle object.
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
    # Constructor: Initializes a new instance of the Square class with equal width and height.
    def __init__(self, side):
        super().__init__(side, side)

    # Method to set all sides of the square.
    def set_side(self, side):
        self.width = self.height = side

    # Override set_width method for the square.
    def set_width(self, width):
        self.set_side(width)

    # Override set_height method for the square.
    def set_height(self, height):
        self.set_side(height)

    # Special method to define the string representation of the Square object.
    def __str__(self):
        return f"Square(side={self.width})"

# Example usage of the polygon area calculator.
rect = Rectangle(10, 5)
print(rect.get_area())  # Output: 50
rect.set_height(3)
print(rect.get_perimeter())  # Output: 26
print(rect)  # Output: Rectangle(width=10, height=3)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())  # Output: 81
sq.set_side(4)
print(sq.get_diagonal())  # Output: 5.656854249492381
print(sq)  # Output: Square(side=4)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))  # Output: 8
