import unittest
from term import *
from unittest import TestCase

class Test_Term(TestCase):

    term1 = Term(Day.TUE, 9, 45)
    term2 = Term(Day.WED, 10, 15)

    pp1 = Term(Day.MON, 21, 45)
    pp2 = Term(Day.THU, 4, 20)

    e1 = Term(Day.THU, 4, 20)

    s1 = Term(Day.THU, 4, 20)


    def test_print(self):
        self.assertEqual(self.term1.__str__(), 'Wtorek 9:45 [90]')
        self.assertEqual(self.term2.__str__(), 'Środa 10:15 [90]')
        self.assertEqual(self.pp1.__str__(), 'Poniedziałek 21:45 [90]')
        self.assertEqual(self.pp2.__str__(), 'Czwartek 4:20 [90]')
        

    def test_earlierThan(self):
        self.assertEqual(self.term1.earlierThan(self.term2), True)
        self.assertEqual(self.term2.earlierThan(self.term1), False)
        self.assertEqual(self.pp1.earlierThan(self.pp2), True)
        self.assertEqual(self.pp2.earlierThan(self.pp1), False)


        

    def test_laterThan(self):
        self.assertEqual(self.term1.laterThan(self.term2), False)
        self.assertEqual(self.term2.laterThan(self.term1), True)
        self.assertEqual(self.pp1.laterThan(self.pp2), False)
        self.assertEqual(self.pp2.laterThan(self.pp1), True)

    def test_equals(self):
        self.assertEqual(self.term1.equals(self.term2), False)
        self.assertEqual(self.pp2.equals(self.e1), True)


    def test_endTime(self):
        self.assertEqual(self.term1.endTime().__str__(), 'Wtorek 11:15 [90]')
        self.assertEqual(self.term2.endTime().__str__(), 'Środa 11:45 [90]')
        self.assertEqual(self.pp1.endTime().__str__(), 'Poniedziałek 23:15 [90]')
        self.assertEqual(self.pp2.endTime().__str__(), 'Czwartek 5:50 [90]')


    def test_setTerm(self):
        self.s1.setTerm("Środa 8:00", 510)
        self.assertEqual(self.s1.__str__(), 'Środa 8:00 [30]')
        self.assertEqual(self.s1.endTime().__str__(), 'Środa 8:30 [30]')

        self.s1.setTerm("Środa 0:00", 1440)
        self.assertEqual(self.s1.__str__(), 'Środa 0:00 [1440]')
        self.assertEqual(self.s1.endTime().__str__(), 'Czwartek 0:00 [1440]')



    
    
if __name__ == '__main__':
    unittest.main()


    