import unittest
from square import area, perimeter  # Импортируем функции из square.py

class SquareTestCase(unittest.TestCase):

    def test_area_positive_side(self):
        res = area(5)
        self.assertEqual(res, 25)

    def test_area_zero_side(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_negative_side(self):
        with self.assertRaises(ValueError) as context:
            area(-4)
        self.assertEqual(str(context.exception), "Ошибка: Сторона квадрата не может быть отрицательной.")

    def test_area_float_side(self):
        res = area(3.5)
        self.assertAlmostEqual(res, 12.25, places=7)

    def test_perimeter_positive_side(self):
        res = perimeter(5)
        self.assertEqual(res, 20)

    def test_perimeter_zero_side(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_negative_side(self):
        with self.assertRaises(ValueError) as context:
            perimeter(-5)
        self.assertEqual(str(context.exception), "Ошибка: Сторона квадрата не может быть отрицательной.")

    def test_perimeter_float_side(self):
        res = perimeter(3.5)
        self.assertAlmostEqual(res, 14, places=7)

if __name__ == '__main__':
    unittest.main()

# python3 -m unittest test_square.py
