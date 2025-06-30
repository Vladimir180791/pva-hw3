from src.square import Square

class TestSquare:
    def test_square_properties(self):
        square = Square(5)
        assert square.area == 25
        assert square.perimeter == 20