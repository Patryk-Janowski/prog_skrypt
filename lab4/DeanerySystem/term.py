from day import Day, nthDayFrom

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

