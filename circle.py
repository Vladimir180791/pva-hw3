from math import pi
from .figure import Figure

class Circle(Figure):
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius

    def get_area(self) -> float:
        return pi * self.radius ** 2

    def get_perimeter(self) -> float:
        return 2 * pi * self.radius