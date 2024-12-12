import math

def area(r):
    ''' Принимает число r, возвращает площадь круга радиуса r. '''
    if r < 0:
        raise ValueError("Ошибка: Радиус не может быть отрицательным.")
    return math.pi * r * r

def perimeter(r):
    ''' Принимает число r, возвращает периметр круга радиуса r. '''
    if r < 0:
        raise ValueError("Ошибка: Радиус не может быть отрицательным.")
    return 2 * math.pi * r
