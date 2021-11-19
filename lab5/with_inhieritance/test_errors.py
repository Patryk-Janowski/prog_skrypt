import unittest
from f_break import Break
from f_timetable2 import Timetable2
from f_lesson import *

class Test(unittest.TestCase):

    t1 = Teacher("Stanislaw", "Polak")
    term1 = Term(9, 45, duration=90)
    b1 = Break(9, 30, duration=15)
    b2 = Break(11, 15, duration=15)
    table1 = Timetable2([b1, b2])
    l1 = Lesson(Term(15, 00, day=Day.WED), "pp", 2, t1)
    l2 = Lesson(Term(17, 00, day=Day.SAT), "aa", 2, t1)
    l3 = Lesson(Term(18, 00, day=Day.SUN), "bb", 2, t1)
    l4 = Lesson(Term(18, 30, day=Day.SUN), "cc", 2, t1)

    t = Timetable2([])
    

    def test_1_put(self):
        self.assertEqual(self.t.put(self.l1), True)
        self.assertEqual(self.t.put(self.l2), True)
        self.assertEqual(self.t.put(self.l3), True)
        self.assertEqual(self.t.put(self.l4), False)
        self.assertEqual(self.t.put(self.l4), False)

    def test_busy(self):
        self.assertEqual(self.t.busy(self.l1.term), True)
        self.assertEqual(self.t.busy(Term(16, 00, day=Day.SAT)), True)
        self.assertEqual(self.t.busy(Term(9,35, day=Day.MON)), False)

    def test_get(self):
        self.assertEqual(self.t.get(Term(9, 15, day=Day.TUE)), None)
        self.assertEqual(self.t.get(self.l2.term), self.l2)

#########################################################################

    def test_lesson(self):
        with self.assertRaises(ValueError):
            l1 = Lesson(Term(23, 00, day=Day.WED), "pp", 2, self.t1)
        with self.assertRaises(ValueError):
            l2 = Lesson(Term(8, 00), "pp", 2, self.t1)

    def test_term(self):
        with self.assertRaises(ValueError):
            term2 = Term(25, 45, duration=90)
        with self.assertRaises(ValueError):
            self.term1.setTerm("aaaaaa", -10)

    def self(self):
        with self.assertRaises(ValueError):
            self.table1.parse(['d+', 'a'])
        with self.assertRaises(ValueError):
            self.table1.perform([])



if __name__ == '__main__':
    unittest.main()