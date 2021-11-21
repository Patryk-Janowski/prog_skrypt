# Utwórz klasę Lesson, która zawiera podane (publiczne) pola, metodę oraz konstruktor:
# pole term typu Term
# pole name typu String
# pole teacherName typu String
# pole year typu int
# pole full_time typu bool, którego wartość jest określana automatycznie, w konstruktorze (patrz informacje zawarte w pkt. 2). Wartość true oznacza, że podane zajęcia są zajęciami na studiach stacjonarnych, zaś false oznacza zajęcia na studiach niestacjonarnych
# konstruktor Lesson(Term term, String name, String teacherName, int year) przypisuje polu term, name, teacherName oraz year podane wartości
# metody: earlierDay(), laterDay(), earlierTime() oraz laterTime():
# metody earlierDay() oraz laterDay() przesuwają zajęcia, odpowiednio, o jeden dzień do tyłu lub do przodu, pod warunkiem, że jest to możliwe, tzn. zmodyfikowany termin spełnia założenia wymienione w punkcie 2
# metody earlierTime() oraz laterTime() przesuwają zajęcia, odpowiednio, o duration minut do tyłu lub do przodu, pod warunkiem, że jest to możliwe
# Metody te zwracają true jeżeli operacja przesunięcia powiodła się, w przeciwnym przypadku zwracają false
# metoda __str__() zwraca napis z informacją o terminie zajęć / lekcji w następującej postaci:
# nazwa_zajęć (dzień_tygodnia godzina_rozpoczęcia-godzina_zakończenia)
# rok i rodzaj studiów
# imię i nazwisko wykładowcy
# przykład użycia:
# lesson = Lesson(Term(9, 35, Day.TUE), "Programowanie skryptowe", "Stanisław Polak", 2);
# print(lesson); """Programowanie skryptowe (Wtorek 9:35-11:05)
#                   Drugi rok studiów stacjonarnych
#                   Prowadzący: Stanisław Polak
#                 """

from term import *
from typing import Dict

class Lesson:

    FRIDAY_MIDNIGHT = Term(24, 00, day=Day.FRI)

    years = dict()
    years[1] = "Pierszy rok studiów"
    years[2] = "Drugi rok studiów"
    years[3] = "Trzeci rok studiów"
    years[4] = "Czwarty rok studiów"
    years[5] = "Piąty rok studiów"
    
    def __init__(self, term: Term, name: str, teacher_name: str, year: int):
        factory = LessonFactory()
        self.__term = term
        self.flywieght = factory.get_flyweight(name, teacher_name, year, self.term.is_full_time(), self.term.is_part_time())

    @property
    def term(self):
        return self.__term

    @property
    def name(self):
        return self.flywieght.name

    @property
    def teacher_name(self):
        return self.flywieght.teacher_name

    @property
    def year(self):
        return self.flywieght.year

    @property
    def part_time(self):
        return self.flywieght.part_time

    @property
    def full_time(self):
        return self.flywieght.full_time


    def __str__(self) -> str:
        if self.full_time:
            full_or_part = "stacjonarnych"
        else:
            full_or_part = "niestacjonarnych"

        return f'''{self.name}, ({self.term.display_day} {self.term.display_start_end})
{Lesson.years[self.year]} {full_or_part}
Prowadzący {self.teacher_name}
'''

    def move_term(self, min):
        new_term = self.term.min_to_instance(self.term.min_from_start + min, duration=self.term.duration)

        if self.full_time and new_term.is_full_time():
            self.term = new_term
            return True
        elif self.part_time and new_term.is_part_time():
            self.term = new_term
            return True
        else:
            return False

    def earlier_day(self):
        return self.move_term(-Term.min_in_day)

    def later_day(self):
        return self.move_term(Term.min_in_day)
    
    def later_term(self):
        return self.move_term(self.term.duration)

    def earlier_term(self):
        return self.move_term(-self.term.duration)


class LessonFlywieght:

    def __init__(self, name: str, teacher_name: str, year: int, full_time, part_time) -> None:
        self.__name = name
        self.__teacher_name = teacher_name
        self.__year = year
        self.__full_time = full_time
        self.__part_time = part_time

    @property
    def name(self):
        return self.__name

    @property
    def teacher_name(self):
        return self.__teacher_name

    @property
    def year(self):
        return self.__year

    @property
    def part_time(self):
        return self.__part_time

    @property
    def full_time(self):
        return self.__full_time


class LessonFactory:

    _lessons = dict()

    def get_key(self, name: str, teacher_name: str, year: int, full_time, part_time):
        return f'{name} {teacher_name} {year} {full_time} {part_time}'


    def get_flyweight(self, name: str, teacher_name: str, year: int, full_time, part_time) -> LessonFlywieght:

        key = self.get_key(name, teacher_name, year, full_time, part_time)

        if not self._lessons.get(key):
            print("LessonFlyweightFactory: Can't find a flyweight, creating new one.")
            self._lessons[key] = LessonFlywieght(name, teacher_name, year, full_time, part_time)
        else:
            print("LessonFlyweightFactory: Reusing existing flyweight.")

        return self._lessons[key]

    def list_lessons(self) -> None:
        count = len(self._lessons)
        print(f"LessonFactory: I have {count} flyweights:")
        for lesson in self._lessons:
            print(lesson)


if __name__ == '__main__':
    factory = LessonFactory()
    l1 = Lesson(Term(15, 00, day=Day.WED), "Stanisław Polak", "Programowanie Skryptowe", 2)
    l2 = Lesson(Term(18, 00, day=Day.MON), "Stanisław Polak", "Programowanie Skryptowe", 2)
    l3 = Lesson(Term(9, 00, day=Day.FRI), "Stanisław Polak", "Programowanie Skryptowe", 2)
    l4 = Lesson(Term(9, 00, day=Day.SAT), "Stanisław Polak", "Programowanie Skryptowe", 2)
    print(l1.flywieght)
    print(l2.flywieght)
    print(l3.flywieght)
    print(l4.flywieght)    
    factory.list_lessons()


