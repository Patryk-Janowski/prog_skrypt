from enum import Enum
from f_day import Day, day_to_name, name_to_day
import re
import f_basic_term



class Term(f_basic_term.BasicTerm):

    min_in_week = 10080
    min_in_day = 1440

    def __init__(self, hour, minute, duration=90, day=Day.NOT_SPECYFIED):
        try:
            assert hour <= 24 and minute < 60 and day.value in range(8)
        except:
            raise ValueError("Hour or minute not in correct range")
        self.__day = day
        super().__init__(hour, minute, duration)
      

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, day):
        self.__day = day


    @property
    def display_day(self):
        return self.__day.to_name


    def __str__(self) -> str:
        return f'{self.display_day} {self.hour}:{self.display_min} [{self.duration}]'


    @property
    def display_day(self):
        return self.__day.to_name


    @property
    def display_start_end(self):
        end = self.endTime()
        return f'{self.hour}:{self.display_min} - {end.hour}:{end.display_min}'


    @property
    def min_from_start(self):
        return self.__day.value * Term.min_in_day + self.hour * 60 + self.minute


    def min_to_instance(self, sum_min: int, duration=90, day_flag=False):
        if sum_min < 0:
            sum_min = self.min_in_week - (abs(sum_min) % self.min_in_week)
        day = sum_min // Term.min_in_day
        sum_min -= day * Term.min_in_day
        hour = sum_min // 60
        sum_min -= hour * 60
        min = sum_min % 60
        day = (day - 1) % 7 + 1
        if day_flag:
            return(Term(hour, min, duration=duration))
        else:
            return Term(hour, min, duration=duration, day=Day(day))


    def endTime(self):
        sum_min = self.min_from_start + self.duration
        if self.__day.value == Day.NOT_SPECYFIED.value:
            return self.min_to_instance(sum_min, duration=self.duration, day_flag=True)
        else:
            return self.min_to_instance(sum_min, duration=self.duration)

    
    @property
    def get_day(self):
        return self.__day


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
            raise ValueError('Wrong data, can not update term')
        else:
            self.__day = Day(name_to_day[day])
            self.hour = hour
            self.minute = minute
            self.duration = duration

    
    def is_full_time(self):
        if self.__day == Day.NOT_SPECYFIED:
            raise ValueError('Day not specyfied')
        if Day.MON.value <= self.__day.value <= Day.THU.value:
            if Term(8, 0, day=self.__day) <= self and self.endTime() <= Term(20, 0, day=self.__day):
                return True
            else:
                return False
        elif self.__day.value == Day.FRI.value:
            if Term(8, 0, day=self.__day) <= self and self.endTime() <= Term(17, 0, day=self.__day):
                return True
            else:
                return False
        else:
            return False


    def is_part_time(self):
        if self.__day == Day.NOT_SPECYFIED:
            raise ValueError('Day not specyfied')
        elif Day.SAT.value <= self.__day.value <= Day.SUN.value:
            if Term(8, 0, day=self.__day) <= self and self.endTime() <= Term(20, 0, day=self.__day):
                return True
            else:
                return False
        elif self.__day.value == Day.FRI.value:
            if Term(17, 0, day=self.__day) <= self and self.endTime() <= Term(20, 0, day=self.__day):
                return True
            else:
                return False
        else:
            return False


    def __add__(self, other):
        min_sum = self.min_from_start + other.min_from_start
        return self.min_to_instance(min_sum)


    def __sub__(self, other): 
        duration = self.endTime().min_from_start - other.min_from_start
        return Term(other.hour, other.minute, duration, self.__day)


    def __lt__(self, other):
        return self.min_from_start < other.min_from_start


    def __gt__(self, other):
        return self.min_from_start > other.min_from_start


    def __le__(self, other):
        return self.min_from_start <= other.min_from_start


    def __ge__(self, other):
        return self.min_from_start >= other.min_from_start


    def __eq__(self, other):
        return self.min_from_start == other.min_from_start and self.duration == other.duration
        
        
def main():
    term1 = Term(8, 30)
    term2 = Term(9, 45, duration=30)
    term3 = Term(9, 45, duration=90)
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
    print(term4)                             # - czas trwania to różnica minut pomiędzy godziną zakończenia 'term3' (11:15), a godziną rozpoczęcia 'term1' (8:30)
                                             # Ma się wypisać "8:30 [165]"


if __name__ == '__main__':
    # main()
    term1 = Term(8, 30)
    print(help(term1))
    l = [1,2,3,4]
