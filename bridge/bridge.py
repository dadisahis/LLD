from abc import ABC, abstractmethod

# Implementor Interface
class Renderer(ABC):
    @abstractmethod
    def render_circle(self, radius: float) -> None:
        pass

    @abstractmethod
    def render_square(self, length: float, width: float) -> None:
        pass

class VectorRenderer(Renderer):
    def render_circle(self, radius):
        print(f"Drawing a circle of radius {radius} using Vector Renderer")
    
    def render_square(self, length, width):
        print(f"Drawing a square of length {length} and width {width} using Vector Renderer")

class RasterRenderer(Renderer):
    def render_circle(self, radius):
        print(f"Drawing a circle of radius {radius} using Raster Renderer")
    
    def render_square(self, length, width):
        print(f"Drawing a square of length {length} and width {width} using Raster Renderer")


# Abstraction
class Shape(ABC):
    def __init__(self, renderer: Renderer):
        self.renderer = renderer

    @abstractmethod
    def draw(self) -> None:
        pass


class Circle(Shape):
    def __init__(self, renderer, radius: float):
        super().__init__(renderer)
        self.radius = radius

    def draw(self) -> None:
        self.renderer.render_circle(self.radius)

class Square(Shape):
    def __init__(self, renderer, length: float, width: float):
        super().__init__(renderer)
        self.length = length
        self.width = width
    
    def draw(self) -> None:
        self.renderer.render_square(self.length, self.width)
        