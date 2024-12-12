import unittest
from triangle import area, perimeter  # Импортируем функции из triangle.py

class TriangleTestCase(unittest.TestCase):

    def test_area_positive_dimensions(self):
        res = area(5, 10)
        self.assertEqual(res, 25)

    def test_area_zero_height(self):
        res = area(5, 0)
        self.assertEqual(res, 0)

    def test_area_zero_base(self):
        res = area(0, 10)
        self.assertEqual(res, 0)

    def test_area_negative_dimensions(self):
        with self.assertRaises(ValueError) as context:
            area(-5, 10)
        self.assertEqual(str(context.exception), "Ошибка: Основание и высота не могут быть отрицательными.")

    def test_perimeter_positive_dimensions(self):
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_perimeter_zero_side(self):
        res = perimeter(0, 4, 5)
        self.assertEqual(res, 9)

    def test_perimeter_negative_side(self):
        with self.assertRaises(ValueError) as context:
            perimeter(-3, 4, 5)
        self.assertEqual(str(context.exception), "Ошибка: Стороны треугольника не могут быть отрицательными.")

    def test_area_float_dimensions(self):
        res = area(2.5, 4.0)
        self.assertAlmostEqual(res, 5.0, places=7)

if __name__ == '__main__':
    unittest.main()

#python3 -m unittest test_triangle.py
