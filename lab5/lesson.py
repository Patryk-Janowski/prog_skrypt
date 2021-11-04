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

    years = dict()
    years[1] = "Pierszy rok studiów"
    years[2] = "Drugi rok studiów"
    years[3] = "Trzeci rok studiów"
    years[4] = "Czwarty rok studiów"
    years[5] = "Piąty rok studiów"
    
    def __init__(self, term: Term, name: str, teacher_name: str, year: int):
        self.term = term
        self.name = name
        self.teacher_name = teacher_name
        self.year = year

        self.full_time = self.term.is_full_time()
        self.part_time = self.term.is_part_time()

        if not self.full_time and not self.part_time:
            raise ValueError('Lesson not in acceptable time')
    

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

lesson = Lesson(Term(17, 35, day=Day.FRI), "Programowanie skryptowe", "Stanisław Polak", 2)

print(lesson)


        


