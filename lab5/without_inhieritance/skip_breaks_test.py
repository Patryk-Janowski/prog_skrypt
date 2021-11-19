import unittest
from f_timetable2 import *
from unittest import TestCase

class TestSkipBreaks(TestCase):
    t1 = Teacher("Stanislaw", "Polak")
    l1 = Lesson(Term(8, 00, day=Day.MON),"pp", 2, t1)
    b1 = Break(Term(9, 30, duration=15))
    b2 = Break(Term(11, 15, duration=15))
    b_list = [b1, b2]
    table = Timetable2(b_list)
    table.put(l1)

    def test_1later_term(self):
        Timetable2.skip_break = True
        self.table.later_term(self.l1)
        self.assertTrue(self.l1.term == Term(9, 45, day=Day.MON))
        self.table.later_term(self.l1)
        self.assertTrue(self.l1.term == Term(11, 30, day=Day.MON))


    def test_2earlier_term(self):
        self.table.earlier_term(self.l1)
        self.assertTrue(self.l1.term == Term(9, 45, day=Day.MON))
        self.table.earlier_term(self.l1)
        self.assertTrue(self.l1.term == Term(8, 00, day=Day.MON))


    def test_3later_term_no_skip(self):
        Timetable2.skip_break = False
        self.table.later_term(self.l1)
        self.assertTrue(self.l1.term == Term(8, 00, day=Day.MON))


    def test_4later_term_no_skip(self):
        Timetable2.skip_break = True
        self.table.later_term(self.l1)
        Timetable2.skip_break = False
        self.table.earlier_term(self.l1)
        self.assertTrue(self.l1.term == Term(9, 45, day=Day.MON))
        


if __name__ == '__main__':
    unittest.main()

