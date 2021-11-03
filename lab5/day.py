#!/usr/bin/env python3

from enum import Enum, auto


day_to_name = dict()
day_to_name[0] = ''
day_to_name[1] = 'Poniedziałek'
day_to_name[2] = 'Wtorek'
day_to_name[3] = 'Środa'
day_to_name[4] = 'Czwartek'
day_to_name[5] = 'Piątek'
day_to_name[6] = 'Sobota'
day_to_name[7] = 'Niedziela'

name_to_day = {v: k for k, v in day_to_name.items()}

class Day(Enum):

    NOT_SPECYFIED = 0
    MON = 1
    TUE = 2
    WED = 3
    THU = 4
    FRI = 5
    SAT = 6
    SUN = 7

    def difference(self, day: Enum):
        diff = day.value - self.value
        if diff > 3:
            return diff - 7
        elif diff < -3:
            return 7 + diff
        else:
            return diff

    @property
    def to_name(self):
        global day_to_name
        return day_to_name[self.value]

def nthDayFrom(n, day: Day):
    new_day = (day.value + n - 1) % 7 + 1
    return Day(new_day)

