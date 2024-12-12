import unittest
from rectangle import area, perimeter  # Импортируем функции из rectangle.py

class RectangleTestCase(unittest.TestCase):

    def test_area_positive_dimensions(self):
        res = area(5, 10)
        self.assertEqual(res, 50)

    def test_area_zero_dimension(self):
        res = area(0, 10)
        self.assertEqual(res, 0)

    def test_area_negative_dimension(self):
        with self.assertRaises(ValueError) as context:
            area(-5, 10)
        self.assertEqual(str(context.exception), "Ошибка: Длины сторон не могут быть отрицательными.")

    def test_area_float_dimensions(self):
        res = area(5.5, 10.5)
        self.assertAlmostEqual(res, 57.75, places=7)

    def test_perimeter_positive_dimensions(self):
        res = perimeter(5, 10)
        self.assertEqual(res, 30)

    def test_perimeter_zero_dimension(self):
        res = perimeter(0, 10)
        self.assertEqual(res, 20)

    def test_perimeter_negative_dimension(self):
        with self.assertRaises(ValueError) as context:
            perimeter(-5, 10)
        self.assertEqual(str(context.exception), "Ошибка: Длины сторон не могут быть отрицательными.")

    def test_perimeter_float_dimensions(self):
        res = perimeter(5.5, 10.5)
        self.assertAlmostEqual(res, 32, places=7)

if __name__ == '__main__':
    unittest.main()


#python3 -m unittest test_rectangle.py
