import pytest
from src.figure import Figure
from src.circle import Circle
from src.rectangle import Rectangle

class TestFigure:
    def test_add_area(self):
        circle = Circle(5)
        rectangle = Rectangle(4, 5)
        assert circle.add_area(rectangle) == circle.area + rectangle.area

    def test_add_area_invalid_type(self):
        circle = Circle(5)
        with pytest.raises(ValueError, match="Переданный объект не является геометрической фигурой."):
            circle.add_area("not a figure")