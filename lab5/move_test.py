from enum import unique
from re import T
from unittest import TestCase
import unittest
from lesson import *

class TestLessonMove(TestCase):

    l1 = Lesson(Term(15, 00, day=Day.WED), "", "", 2)
    l2 = Lesson(Term(17, 00, day=Day.SAT), "", "", 2)

    def setUp(self):
        self.l1 = Lesson(Term(15, 00, day=Day.WED), "", "", 2)
        self.l2 = Lesson(Term(17, 00, day=Day.SAT), "", "", 2)

    
    def test_later_term(self):
        for _ in range(2):
            self.assertEqual(self.l1.later_day(), True)
        self.assertEqual(self.l1.later_day(), False)
        self.assertEqual(self.l1.term == Term(15, 00, day=Day.FRI), True)

        self.assertEqual(self.l2.later_day(), True)
        self.assertEqual(self.l2.later_day(), False)
        self.assertEqual(self.l2.term == Term(17, 00, day=Day.SUN), True)


    def test_earlier_term(self):
        for _ in range(2):
            self.assertEqual(self.l1.earlier_day(), True)
        self.assertEqual(self.l1.earlier_day(), False)
        self.assertEqual(self.l1.term == Term(15, 00, day=Day.MON), True)

        self.assertEqual(self.l2.earlier_day(), True)
        self.assertEqual(self.l2.earlier_day(), False)
        self.assertEqual(self.l2.term ==  Term(17, 00, day=Day.FRI), True)

    
    def test_earlier_term(self):
        for _ in range(4):
            self.assertEqual(self.l1.earlier_term(), True)
        self.assertEqual(self.l1.earlier_term(), False)
        self.assertEqual(self.l1.term == Term(9, 00, day=Day.WED), True)

        for _ in range(6):
            self.assertEqual(self.l2.earlier_term(), True)
        self.assertEqual(self.l2.earlier_term(), False)
        self.assertEqual(self.l2.term ==  Term(8, 0, day=Day.SAT), True)


    def test_later_term(self):
        for _ in range(2):
            self.assertEqual(self.l1.later_term(), True)
        self.assertEqual(self.l1.later_term(), False)
        self.assertEqual(self.l1.term == Term(18, 00, day=Day.WED), True)

        
        self.assertEqual(self.l2.later_term(), True)
        self.assertEqual(self.l2.later_term(), False)
        self.assertEqual(self.l2.term ==  Term(18, 30, day=Day.SAT), True)



if __name__ == '__main__':
    unittest.main()