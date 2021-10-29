from day import Day, nthDayFrom, day_to_name, name_to_day
import re



class Term:

    def __init__(self, day: Day, hour, minute, duration=90):
            self.__day = day
            self.hour = hour
            self.minute = minute
            self.duration = duration

    def __str__(self) -> str:
        return f'{self.__day.to_name()} {self.hour}:{self.minute} [{self.duration}]'


    @property
    def get_day(self):
        return self.__day.value


    def equals(self, other):
        if self.__day.value == other.__day.value and self.hour == other.hour and self.minute == other.minute:
            return True
        else:
            return False


    def earlierThan(self, other):
    
        if self.__day.value < other.__day.value:
            return True
        elif self.__day.value > other.__day.value:
            return False
        else:     
            if self.hour < other.hour:
                return True
            elif self.hour > other.hour:
                return False
            else:
                if self.minute < other.minute:
                    return True
                elif self.minute > other.minute:
                    return False
                else:
                    return False
    

    def laterThan(self, other):
        if not self.equals(other):
            return not self.earlierThan(other)
        else:
            return False


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

        assert day in name_to_day.keys()

        try:
            hour, minute = int(hour), int(minute)
            assert hour <= 24 and minute <= 60
        except:
            print('Wrong data, can not update term')
            return

        self.__day = Day(name_to_day[day])
        self.hour = int(hour)
        self.minute = int(minute)
        self.duration = min_from_mid - self.hour * 60 - self.minute

x =  Term(Day.MON, 10, 10, 124)

x.setTerm("Środa 00:69", 212)

term1 = Term(Day.TUE, 9, 45)
term2 = Term(Day.WED, 10, 15)

pp1 = Term(Day.MON, 21, 45)
pp2 = Term(Day.THU, 4, 20)

e1 = Term(Day.THU, 4, 20)

print(term1.endTime())
print(term2.endTime())
print(pp1.endTime())
print(pp2.endTime())