#!/usr/bin/env python3

import sys


def print_prompt():
    print('''suported opperations:
    a - add course [course_name]
    a - add user [course_name] [user name]
    d - delete user [course_name] [user_name]
    d - delete course [course_name]
    m - modify course name [old_name] [new_name]
    p - print users [course_name]
    CTRL + D to exit
    course name can not contain spaces''')


def add_user_or_course(course_list, params):
    if len(params) == 1:
        if params[0] in course_list.keys():
            print(f'- course {params[0]} already exist')
        else:
            course_list[params[0]] = set()
            print(f'- course {params[0]} added')

    elif len(params) > 1:
        usr_name = ' '.join(params[1:])
        if params[0] not in course_list.keys():
            print(f'- there is no course: {params[0]}')
        elif usr_name in course_list[params[0]]:
            print(f'- user {usr_name} already exist in {params[0]}')
        elif len(course_list[params[0]]) < course_list['max_num']:
            course_list[params[0]].add(usr_name)
            print(f'- user {usr_name} added to {params[0]}')
        else:
            print('- max num of users exceded')
        

def del_user_or_course(course_list, params):
    if len(params) == 1:
        try:
            del course_list[params[0]]
        except KeyError:
            print(f'- course {params[0]} does not exist')
        else:
            print(f'- course: {params[0]} is deleted')

    elif len(params) > 1:
        usr_name = ' '.join(params[1:])
        if params[0] in course_list.keys():
            try:
                course_list[params[0]].remove(usr_name)
            except KeyError:
                print(f'- user {usr_name} is not in course {params[0]}')
            else:
                print(f'- user {usr_name} is deleted from course {params[0]}')
        else:
            print(f'- course: {params[0]} does not exist')


def modify_name(course_list, params):
    if len(params) != 2:
        print('- enter old and new course name (course names can not contain spaces)')
    elif params[0] not in course_list.keys():
        print(f'- there is no course named {params[0]}')
    else:
        course_list[params[1]] = course_list[params[0]]
        del course_list[params[0]]
        print(f'course {params[0]} changed to {params[1]}')
             

def print_course(course_list, params):
    if len(params) == 1 and (params[0] in course_list.keys() or params[0] == 'all'):
        if params[0] == 'all':
            value = list()
            for key, value in course_list.items():
                print(f'{key} -- {value}')
        else:
            print(course_list[params[0]])
    else:
        print('- enter correct course name')
    

def modify_courses(course_list):
    while True:
        try:
            input_data = input('enter operation: ')
            if not input_data:
                break
            else:
                input_data = input_data.split(' ')
                assert len(input_data) >= 2
        except EOFError:
            print('\n- exiting')
            break
        except Exception:
            print('- enter correct commands')
            break
        else:
            option = input_data[0]
            params = input_data[1:]
            if option == 'a':
                add_user_or_course(course_list, params)
            elif option == 'd':
                del_user_or_course(course_list, params)
            elif option == 'p':
                print_course(course_list, params)
            elif option == 'm':
                modify_name(course_list, params)
            else:
                print('- enter supported option')
    return course_list


if __name__ == '__main__':
    try:
        len(sys.argv) == 2
        max_num = int(sys.argv[1])
    except Exception:
        print('wrong parameter, set max num to default value of 10')
        max_num = 10

    course_list = {'max_num' : max_num}
    print_prompt()
    modify_courses(course_list)

    




    
