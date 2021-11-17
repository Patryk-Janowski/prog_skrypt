import unittest
from f_lesson import *
from unittest import TestCase

class TestLessonAndTeacher(TestCase):
    
    t1 = Teacher("Stanislaw", "Polak")
    students = list()
    l1 = Lesson(Term(15, 00, day=Day.WED), "pp", 2, t1)
    l2 = Lesson(Term(15, 00, day=Day.SAT), "programowanie skryptowe", 3, t1)
  
    for x in range(13):
        students.append(Student('lesson 1 student ', str(x)))

    def test_add__student(self):
        for x in range(12):
            self.assertEqual(self.t1.add_student(self.l1.name, self.students[x]), True)
        self.assertEqual(self.t1.add_student(self.l1.name, self.students[12]), False)
        self.assertEqual(len(self.t1.lessons[self.l1.name]), 12)

        for x in range(6):
            self.assertEqual(self.t1.add_student(self.l2.name, self.students[x]), True)
        self.t1.print_all_lessons()

    def test_remove_student(self):
        for x in range(12):
            self.assertEqual(self.t1.remove_student(self.l1.name, self.students[x]), True)
        self.assertEqual(self.t1.remove_student(self.l1.name, self.students[12]), False)
        self.assertEqual(len(self.t1.lessons[self.l1.name]), 0)

    
        
if __name__ == '__main__':
    unittest.main()