#!/usr/bin/env python3

import unittest
import ex_1

dic = dict()
dic.pop('janusz')

if 'jan pawel' in dic.keys():
    print('jan pawel')

class Test_ModifyCourse(unittest.TestCase):

    course_description = {'name' : 'prog', 'time' : '11:15'}
    course = {'info' : course_description, 'max_num' : 5, 'users' : set()}

    