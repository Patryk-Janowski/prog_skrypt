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

class Lesson:

    FRIDAY_MIDNIGHT = Term(24, 00, day=Day.FRI)

    def __init__(self, term: Term, name: str, teacher_name: str, year: int):
        self.term = term
        self.name = name
        self.teacher_name = teacher_name
        self.year = year

        if self.term >  self.__class__.FRIDAY_MIDNIGHT:
            self.full_time = False
        else:
            self.full_time = True

    def is_fult_time(self):
        i


