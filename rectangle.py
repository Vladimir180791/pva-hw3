from .figure import Figure

class Rectangle(Figure):
    def __init__(self, length: float, width: float):
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive")
        self.length = length
        self.width = width

    def get_area(self) -> float:
        return self.length * self.width

    def get_perimeter(self) -> float:
        return 2 * (self.length + self.width)