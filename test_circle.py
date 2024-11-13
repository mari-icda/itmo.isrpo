import unittest
from circle import area, perimeter  # Импортируем функции из circle.py

class CircleTestCase(unittest.TestCase):

    def test_area_zero_radius(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_positive_radius(self):
        res = area(10)
        self.assertAlmostEqual(res, 314.1592653589793, places=7)

    def test_area_negative_radius(self):
        with self.assertRaises(ValueError) as context:
            area(-5)
        self.assertEqual(str(context.exception), "Ошибка: Радиус не может быть отрицательным.")

    def test_area_float_radius(self):
        res = area(5.5)
        self.assertAlmostEqual(res, 95.03317777109125, places=7)

    def test_area_large_radius(self):
        res = area(1000)
        self.assertAlmostEqual(res, 3141592.653589793, places=7)

    def test_perimeter_zero_radius(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_positive_radius(self):
        res = perimeter(10)
        self.assertAlmostEqual(res, 62.83185307179586, places=7)

    def test_perimeter_negative_radius(self):
        with self.assertRaises(ValueError) as context:
            perimeter(-5)
        self.assertEqual(str(context.exception), "Ошибка: Радиус не может быть отрицательным.")

    def test_perimeter_float_radius(self):
        res = perimeter(5.5)
        self.assertAlmostEqual(res, 34.55751918948772, places=7)

    def test_perimeter_large_radius(self):
        res = perimeter(1000)
        self.assertAlmostEqual(res, 6283.185307179586, places=7)

if __name__ == '__main__':
    unittest.main()

# python3 -m unittest test_circle.py