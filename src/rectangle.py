from .figure import Figure

class Rectangle(Figure):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    @property
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

    @property
    def area(self) -> float:
        return self.width * self.height