from src.triangle import Triangle
from src.square import Square

# Создаем фигуры
square = Square(10)
triangle = Triangle(13, 14, 15)

# Выводим площади
print(square.area)          # 100
print(triangle.area)        # 84

# Сумма площадей
print(triangle.add_area(square))  # 184