from src.rectangle import Rectangle

class TestRectangle:
    def test_area_and_perimeter(self):
        rect = Rectangle(4, 5)
        assert rect.area == 20
        assert rect.perimeter == 18