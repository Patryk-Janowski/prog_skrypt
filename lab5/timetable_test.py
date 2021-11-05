import unittest
from lesson import *
from term import *
from day import *
from timetable import *

class test_timetable(unittest.TestCase, Timetable):
    l1 = Lesson(Term(15, 00, day=Day.WED), "", "", 2)
    l2 = Lesson(Term(17, 00, day=Day.SAT), "", "", 2)
    l3 = Lesson(Term(18, 00, day=Day.SUN), "", "", 2)
    l4 = Lesson(Term(18, 30, day=Day.SUN), "", "", 2)

    t = Timetable()
    

    def test_str(self):
        pass

    def test_1_put(self):
        self.assertEqual(self.t.put(test_timetable.l1), True)
        self.assertEqual(self.t.put(test_timetable.l2), True)
        self.assertEqual(self.t.put(test_timetable.l3), True)
        self.assertEqual(self.t.put(test_timetable.l4), False)
        self.assertEqual(self.t.put(test_timetable.l4), False)

    def test_parse(self):
        self.assertEqual(self.t.parse(['d-', 'pavn', 'd+', '+d', 't-', 't+']), [Action.DAY_EARLIER, Action.DAY_LATER, Action.TIME_EARLIER, Action.TIME_LATER])

    def test_busy(self):
        self.assertEqual(self.t.busy(test_timetable.l1.term), True)
        self.assertEqual(self.t.busy(Term(16, 00, day=Day.SAT)), True)
        self.assertEqual(self.t.busy(Term(9,35, day=Day.MON)), False)

    def test_get(self):
        self.assertEqual(self.t.get(Term(9, 15, day=Day.TUE)), None)
        self.assertEqual(self.t.get(test_timetable.l2.term), test_timetable.l2)


    

if __name__ == '__main__':
    unittest.main()