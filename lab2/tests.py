#!/usr/bin/env python3

from unittest import TestCase, mock
import unittest
import ex_1



class Test_ModifyCourse(TestCase):

    max_num = 3

    def setUp(self):
        self.course_list = {'max_num' : self.max_num}

    def tearDown(self):
        del self.course_list
        del self.output_list
        print('-' * 30)


    def test_create_course(self):
        with mock.patch('ex_1.input') as mock_input:
            self.output_list = iter(['a pp', 'a pp1', 'a pp2', None])
            mock_input.side_effect = lambda x : next(self.output_list)
            ex_1.modify_courses(self.course_list)
            self.assertEqual(self.course_list, {'max_num': 3, 'pp': set(), 'pp1': set(), 'pp2': set()})


    def test_create_and_del_course(self):
        with mock.patch('ex_1.input') as mock_input:
            self.output_list = iter(['a pp', 'a pp1', 'd pp', None])
            mock_input.side_effect = lambda x : next(self.output_list)
            ex_1.modify_courses(self.course_list)
            self.assertEqual(self.course_list, {'max_num': 3, 'pp1': set()})


    def test_add_to_much_users(self):
        with mock.patch('ex_1.input') as mock_input:
            self.output_list = iter(['a pp', 'a pp u1', 'a pp u2', 'a pp u3', 'a pp u4', None])
            mock_input.side_effect = lambda x : next(self.output_list)
            ex_1.modify_courses(self.course_list)
            self.assertEqual(self.course_list, {'max_num': 3, 'pp': {'u1', 'u3', 'u2'}})
            

    def test_not_existing_course(self):
        with mock.patch('ex_1.input') as mock_input:
            self.output_list = iter(['a pp', 'a p1', 'd p2', None])
            mock_input.side_effect = lambda x : next(self.output_list)
            ex_1.modify_courses(self.course_list)
            self.assertEqual(self.course_list, {'max_num': 3, 'p1': set(), 'pp': set()})

    
    def test_not_existing_user(self):
        with mock.patch('ex_1.input') as mock_input:
            self.output_list = iter(['a pp', 'a pp u1', 'd pp u2', None])
            mock_input.side_effect = lambda x : next(self.output_list)
            ex_1.modify_courses(self.course_list)
            self.assertEqual(self.course_list, {'max_num': 3, 'pp': {'u1'}})
    

    def test_rename(self):
        with mock.patch('ex_1.input') as mock_input:
            self.output_list = iter(['a pp', 'm pp p1', None])
            mock_input.side_effect = lambda x : next(self.output_list)
            ex_1.modify_courses(self.course_list)
            self.assertEqual(self.course_list, {'max_num': 3, 'p1': set()})

    

if __name__ == '__main__':
    
    unittest.main()