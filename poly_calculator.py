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
