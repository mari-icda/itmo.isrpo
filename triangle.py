def area(a, h):
    ''' Принимает числа a, h, возвращает площадь треугольника. '''
    if a < 0 or h < 0:
        raise ValueError("Ошибка: Основание и высота не могут быть отрицательными.")
    return a * h / 2 

def perimeter(a, b, c):
    ''' Принимает числа a, b, c, возвращает периметр треугольника. '''
    if a < 0 or b < 0 or c < 0:
        raise ValueError("Ошибка: Стороны треугольника не могут быть отрицательными.")
    return a + b + c
