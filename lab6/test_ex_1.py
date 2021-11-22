from unittest import TestCase, main
from ex_1 import Operacje

class test(TestCase):

    def test_correct(self):
        self.assertEqual(Operacje.roznica(self), 6)
        self.assertEqual(Operacje.suma(self, 3, 3), 5)
        self.assertEqual(Operacje.suma(self, 3, 3, 3), 4)

    def test_incorrect(self):
        self.assertRaises(TypeError, Operacje.suma, self)
        self.assertRaises(TypeError, Operacje.suma, self, 1,2,3,4)
        self.assertRaises(TypeError, Operacje.roznica, self, 1,2,3)

    def test_list_change(self):
        op = Operacje()
        self.assertEqual(op.argumentySuma, [4, 5])
        op['suma']=[11,22]
        self.assertEqual(op.argumentySuma, [11, 22])
        self.assertEqual(op.argumentyRoznica, [4, 5, 6])
        op['roznica']=[111,222,333,444]
        self.assertEqual(op.argumentyRoznica, [111, 222, 333, 444])


if __name__ == '__main__':
    main()