#!/usr/bin/env python3

from enum import Enum, auto


class Day(Enum):

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
    


def nthDayFrom(n, day: Day):
    new_day = (day.value + n - 1) % 7 + 1
    if new_day == 1:
        return Day.MON
    elif new_day == 2:
        return Day.TUE
    elif new_day == 3:
        return Day.WED
    elif new_day == 4:
        return Day.THU
    elif new_day == 5:
        return Day.FRI
    elif new_day == 6:
        return Day.SAT
    elif new_day == 7:
        return Day.SUN

x = Day.MON

print(type(x))