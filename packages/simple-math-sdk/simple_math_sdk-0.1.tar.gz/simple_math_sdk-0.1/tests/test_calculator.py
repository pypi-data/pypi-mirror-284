import unittest
from simple_math import Calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        # Uji penjumlahan dua angka positif
        self.assertEqual(Calculator.add(5, 3), 8)
        # Uji penjumlahan angka positif dan negatif
        self.assertEqual(Calculator.add(-1, 1), 0)
        # Uji penjumlahan dua angka negatif
        self.assertEqual(Calculator.add(-1, -1), -2)
        # Uji penjumlahan dengan nol
        self.assertEqual(Calculator.add(0, 5), 5)
        self.assertEqual(Calculator.add(5, 0), 5)

if __name__ == '__main__':
    unittest.main()
