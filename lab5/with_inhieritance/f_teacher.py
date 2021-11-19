import f_student
from f_student import Student

class Teacher:
    def __init__(self, first_name, second_name, lessons=dict()) -> None:

        self.first_name = first_name
        self.second_name = second_name
        self.lessons = lessons


    def add_student(self, lesson_name, student: Student):
        if lesson_name not in self.lessons.keys():
            self.lessons[lesson_name] = set()
        if student not in self.lessons[lesson_name] and len(self.lessons[lesson_name]) < 12:
            self.lessons[lesson_name].add(student)
            return True
        else:
            return False

    def remove_student(self, lesson_name, student: Student):
        if lesson_name not in self.lessons.keys():
            return False
        elif student in self.lessons[lesson_name]:
            self.lessons[lesson_name].remove(student)
            return True
        else:
            return False

    @property
    def full_name(self):
        return f'{self.first_name} {self.second_name}'

    def print_lessons(self, lesson_name):
        r = f'Przedmiot {lesson_name}:'
        assert lesson_name in self.lessons.keys()
        for s in self.lessons[lesson_name]:
            r += f' {s.__str__()},'
        return r
        
    def print_all_lessons(self):
        r = f'wszystkie lekcje prowadzącego: '
        for k in self.lessons.keys():
            r += self.print_lessons(k) + '\n'
        return r

            


    def __str__(self) -> str:
        return f'''Prowadzący: {self.full_name} {self.print_all_lessons()}'''