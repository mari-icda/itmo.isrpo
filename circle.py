import math
'''добавление библиотеки math для использования константы math.pi'''

def area(r):
    ''' Принимает число r, возвращает произведения квадрата числа и числа пи (площадь круга радиуса r) '''
    return math.pi * r * r


def perimeter(r):
    ''' Принимает число r, возвращает произведения удвоенного числа и числа пи (периметр круга радиуса r) '''
    return 2 * math.pi * r

