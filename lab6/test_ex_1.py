from unittest import TestCase, main
from ex_1 import Operacje

class test(TestCase):

    Operacje.argumentySuma = [4,5]
    Operacje.argumentyRoznica = [4,5,6]

    def test_operations(self):
        self.assertEqual(Operacje.roznica(self), 6)
        self.assertEqual(Operacje.roznica(self, 1), 5)
        self.assertEqual(Operacje.roznica(self, 1, 2), 4)
        self.assertEqual(Operacje.suma(self, 1), None)
        self.assertEqual(Operacje.suma(self, 1, 2), 5)
        self.assertEqual(Operacje.suma(self, 1, 2, 3), 4)

    def test_errors(self):
        self.assertRaises(TypeError, Operacje.suma, self)
        self.assertRaises(TypeError, Operacje.suma, self, 1,2,3,4)
        self.assertRaises(TypeError, Operacje.roznica, self, 1,2,3)

    def test_assigment(self):
        op = Operacje()
        op['suma']=[37,21]
        self.assertEqual(op.argumentySuma, [37, 21])
        op['roznica']=[4,2,0]
        self.assertEqual(op.argumentyRoznica, [4,2,0])


if __name__ == '__main__':
    main()