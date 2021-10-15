#!/usr/bin/env python3

import sys

#add option to modify multiple courses 
def modify_course(course):
    print('suported opperations: a - add user, d -delete user, m -modify course name, CTRL + D to exit')

    while True:
        try:
            input_data = input('enter operation: ').split(' ')
        except EOFError:
            print('\nexiting')
            break
        if input_data[0] == 'a':
            usr_name = ' '.join(input_data[1:])
            if len(course['users']) >= course['max_num']:
                print('execeded max num')
            elif usr_name not in course['users']:
                course['users'].add(usr_name)
                print(f'user: {usr_name} was added')
            else:        
                print(f'user: {usr_name} was already in course')
        elif input_data[0] == 'd':
            try:
                course['users'].remove(usr_name)
            except Exception:
                print(f'cannot delete {usr_name}')
            else:
                print(f'user: {usr_name} is deleted')
        elif input_data[0] == 'm':
            course['info']['name'] = ' '.join(input_data)
        else:
            print('enter supported opperation')
    return course


if __name__ == '__main__':

    try:
        len(sys.argv) == 2
        max_num = int(sys.argv[1])
    except Exception:
        print('wrong parameter, set max num to default value of 10')
        max_num = 10

    course_description = {'name' : 'prog', 'time' : '11:15'}
    course = {'info' : course_description, 'max_num' : max_num, 'users' : set()}
    print(modify_course(course))




    
