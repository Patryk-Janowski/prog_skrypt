#!/usr/bin/env python3

from fractions import Fraction
import main
import unittest


class Test_TestIncrementDecrement(unittest.TestCase):

    fr1 = Fraction(3, 5)
    fr2 = Fraction(5, 3)
    fr_sum = Fraction(34, 15)

    im1 = complex(1, 1)
    im2 = complex(2, 5)
    im_sum = complex(3, 6)

    fr1_im1_sum = complex(1.6, 1)

    
    def test_sum_integer_integer(self):
        self.assertEqual(main.sum(2, 2), 4)

    def test_sum_integer_float(self):
        self.assertEqual(main.sum(2, 1.5), 3.5)

    def test_sum_integer_string(self):
       self.assertEqual(main.sum(2, '2'), 4)

    def test_sum_string_string(self):
        self.assertEqual(main.sum('2.1', '2.0'), 4.1)

    def test_sum_float_fraction(self):
        self.assertEqual(main.sum(self.fr1, 2.5), 3.1)

    def test_sum_imag_float(self):
        self.assertEqual(main.sum(self.im1, 2.4), complex(3.4, 1))

    def test_sum_imag(self):
        self.assertEqual(main.sum(self.im1, self.im2), self.im_sum)

    def test_sum_fraction(self):
        self.assertEqual(main.sum(self.fr1, self.fr2), self.fr_sum)

    def test_sum_imag_fraction(self):
        self.assertEqual(main.sum(self.im1, self.fr1), self.fr1_im1_sum)

    def test_sum_integer_wrong_number_in_string(self):
        with self.assertRaises(ValueError):
            main.sum(2, 'Ala ma kota123')

    def test_sum_integer_wrong_input(self):
        with self.assertRaises(TypeError):
            main.sum(1, [2, 3])




if __name__ == '__main__':
    unittest.main()