from  student import Student

class Teacher:
    def __init__(self, first_name, second_name, student_list=set()) -> None:
        self.first_name = first_name
        self.second_name = second_name
        self.student_list = student_list

    def add_student(self, student: Student):
        if student not in self.student_list and len(self.student_list) < 12:
            self.student_list.add(student)
            return True
        else:
            return False

    def remove_student(self, student):
        if student in self.student_list:
            self.student_list.add(student)
            return True
        else:
            return False

    def __str__(self) -> str:
        return f'''Prowadzący: {self.first_name} {self.second_name}
lista uczestników {[x.__str__() for x in self.student_list]}'''