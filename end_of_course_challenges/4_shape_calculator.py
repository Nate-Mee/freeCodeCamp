import math
import re

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            picture = ''
            for num in range(0, int(self.height)):
                picture += ('*' * self.width) + '\n'
            return picture

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
                
    def get_amount_inside(self, shape):
        parts = re.split(r'[=,]', str(shape))
        if 'Rectangle(width' in parts:
            shape_width = int(parts[1])
            shape_height = int(parts[3].rstrip(')'))
        else:
            shape_height = shape_width = int(parts[1].rstrip(')'))
        fit_width = math.floor(self.width / shape_width)
        fit_height = math.floor(self.height / shape_height)
        return int(fit_width * fit_height)


class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

    def set_side(self, side):
        self.width = side
        self.height = side
        
    def __str__(self):
        return f"Square(side={self.width})"

    def set_width(self, side):
        self.width = side
        self.height = side

    def set_height(self, side):
        self.width = side
        self.height = side

rect = Rectangle(4, 8)
answer = Rectangle.get_amount_inside(rect, rect)
print(answer)