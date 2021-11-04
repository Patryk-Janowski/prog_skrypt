from unittest import TestCase
from lesson import *

class TestLessonMove(TestCase):

    l1 = None
    l2 = None
    l3 = None

    def setUp(self):
        self.__class__.l1 = Lesson(Term(17, 35, day=Day.FRI), "Programowanie skryptowe", "Stanisław Polak", 2)
        self.__class__.l2 = Lesson(Term(17, 35, day=Day.FRI), "Programowanie skryptowe", "Stanisław Polak", 2)
        self.__class__.l3 = Lesson(Term(17, 35, day=Day.FRI), "Programowanie skryptowe", "Stanisław Polak", 2)

    
    