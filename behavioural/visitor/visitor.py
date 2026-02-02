from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius
    def accept(self, visitor):
        visitor.visit_circle(self)

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def get_side(self):
        return self.side

    def accept(self, visitor):
        visitor.visit_square(self)

class ShapeVisitor(ABC):
    @abstractmethod
    def visit_circle(self, circle):
        pass

    @abstractmethod
    def visit_square(self, square):
        pass

class AreaCalculator(ShapeVisitor):
    def visit_circle(self, circle):
        area   = 3.14 * (circle.get_radius()**2)
        print(f"Area of Circle: {area}")
    def visit_square(self, square):
        area = square.get_side() ** 2
        print(f"Area of Square: {area}")

class SVGEXporter(ShapeVisitor):
    def visit_circle(self, circle):
        svg = f'<circle r="{circle.get_radius()}" />'
        print(f"SVG for Circle: {svg}")

    def visit_square(self, square):
        svg = f'<rect width="{square.get_side()}" height="{square.get_side()}" />'
        print(f"SVG for Square: {svg}")