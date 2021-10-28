from day import Day, nthDayFrom

class Term:

    def __init__(self, day: Day, hour, minute, duration=90):
            self.__day = day
            self.hour = hour
            self.minute = minute
            self.duration = duration

    def __str__(self) -> str:
        return f'{self.__day.to_name()} {self.hour}:{self.minute}:{self.duration}'

    
pp = Term(Day.MON, 1, 1)
print(pp)
        