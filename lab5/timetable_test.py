import unittest
from lesson import *
from term import *
from day import *
from timetable import *

class test_timetable(unittest.TestCase):
    tablica = [Lesson(Term(10, 15, day=Day.TUE), "Programowanie skryptowe", "Stanisław Polak", 2), Lesson(Term(8, 00, day=Day.TUE), "Informatyka śledcza", "Kamil Jurczyk", 2)]
    busy = Timetable1.busy

    def test_str(self):
        pass

    def test_parse(self):
        self.assertEqual(Timetable1.parse(self, ['d-', 'fekali', 'd+', '+d', 't-', 't+']), ['DAY_EARLIER', 'DAY_LATER', 'TIME_EARLIER', 'TIME_LATER'])

    def test_busy(self):
        self.assertEqual(Timetable1.busy(self, Term(9,35, day=Day.TUE)), True)
        self.assertEqual(Timetable1.busy(self, Term(9,00, duration=300, day=Day.TUE)), True)
        self.assertEqual(Timetable1.busy(self, Term(9,35, day=Day.MON)), False)

    def test_get(self):
        self.assertEqual(Timetable1.get(self, Term(9, 15, day=Day.TUE)), None)
        self.assertEqual(Lesson.por(Timetable1.get(self, Term(8, 00, day=Day.TUE)), Lesson(Term(8, 00, day=Day.TUE), "Informatyka śledcza", "Kamil Jurczyk", 2)), True)

    def test_put(self):
        self.assertEqual(Timetable1.put(self, Lesson(Term(10, 15, day=Day.TUE), "Programowanie skryptowe", "Stanisław Polak", 2)), False)
        self.assertEqual(Timetable1.put(self, Lesson(Term(10, 15, day=Day.WED), "Programowanie skryptowe", "Stanisław Polak", 2)), True)

if __name__ == '__main__':
    unittest.main()