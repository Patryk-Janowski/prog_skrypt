from enum import Enum
from day import Day, nthDayFrom, day_to_name, name_to_day
import re



class Term:

    min_in_week = 11520

    def __init__(self, day: Day, hour, minute, duration=90):
            self.__day = day
            self.hour = hour
            self.minute = minute
            self.duration = duration


    def __str__(self) -> str:
        return f'{self.__day.to_name()} {self.hour}:{self.display_min} [{self.duration}]'


    @property
    def get_day(self):
        return self.__day.value


    @property
    def display_min(self):
        if self.minute < 10:
            return '0' + str(self.minute)
        else:
            return str(self.minute)


    def equals(self, other):
        if self.__day.value == other.__day.value and self.hour == other.hour and self.minute == other.minute:
            return True
        else:
            return False


    @property
    def min_from_start(self):
        return self.get_day * 1440 + self.hour * 60 + self.minute


    def min_to_instance(self, sum_min: int):
        if sum_min < 0:
            sum_min = (self.min_in_week - (self.min_in_week % abs(sum_min)))
        day = sum_min // 1440
        sum_min -= day * 1440
        hour = sum_min // 60
        sum_min -= hour * 60
        min = sum_min % 60
        day = day % 6 + 1
        return Term(Day(day), hour, min)


    def endTime(self):
        sum_min = self.minute + self.duration
        plus_h = sum_min // 60
        minute = sum_min % 60
        sum_hour = self.hour + plus_h
        if sum_hour >= 24:
            day = Day(self.__day.value + sum_hour // 24)
        else:
            day = Day(self.__day.value)
        hour = sum_hour % 24
        return Term(day, hour, minute, self.duration)


    def setTerm(self, description, min_from_mid):
        day = re.findall(r'^\w+\b', description)[0]
        hour, minute = re.findall(r'\b\d{1,2}', description)
        try:
            assert day in name_to_day.keys()
            hour, minute = int(hour), int(minute)
            assert hour <= 24 and minute <= 60
            duration = min_from_mid - hour * 60 - minute
            assert duration >= 0
        except:
            print('Wrong data, can not update term')
        else:
            self.__day = Day(name_to_day[day])
            self.hour = hour
            self.minute = minute
            self.duration = duration
    

    def __add__(self, other):
        min_sum = self.min_from_start + other.min_from_start
        return self.min_to_instance(min_sum)


    def __sub__(self, other): 
        min_sum = self.min_from_start - other.min_from_start
        return self.min_to_instance(min_sum)


    def __lt__(self, other):
        return self.min_from_start < other.min_from_start


    def __gt__(self, other):
        return self.min_from_start > other.min_from_start


    def __le__(self, other):
        return self.min_from_start <= other.min_from_start


    def __ge__(self, other):
        return self.min_from_start >= other.min_from_start


    def __eq__(self, other):
        return self.min_from_start == other.min_from_start
        

if __name__ == '__main__':
    term1 = Term(8, 30)
    term2 = Term(9, 45, 30)
    term3 = Term(9, 45, 90)
    print(term1)                             # Ma się wypisać: "8:30 [90]"
    print(term2)                             # Ma się wypisać: "9:45 [30]"
    print(term3)                             # Ma się wypisać: "9:45 [90]"
    print("term1 < term2:", term1 < term2)   # Ma się wypisać True
    print("term1 <= term2:", term1 <= term2) # Ma się wypisać True
    print("term1 > term2:", term1 > term2)   # Ma się wypisać False
    print("term1 >= term2:", term1 >= term2) # Ma się wypisać False
    print("term2 == term2:", term2 == term2) # Ma się wypisać True
    print("term2 == term3:", term2 == term3) # Ma się wypisać False
    term4 = term3 - term1                    # Tworzy termin, którego:
                                            # - godzina rozpoczęcia jest taka jak 'term1',
                                            # - czas trwania to różnica minut pomiędzy godziną zakończenia 'term3' (11:15), a godziną rozpoczęcia 'term1' (8:30)
    print(term4)                             # Ma się wypisać "8:30 [165]"