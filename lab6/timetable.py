from term import *
from lesson import *
from typing import List
from action import *

class Timetable:

    lesson_list = list()
    busy_set = list()
    action_set = dict()
    action_set['d+'] = Action.DAY_LATER
    action_set['d-'] = Action.DAY_EARLIER
    action_set['t+'] = Action.TIME_LATER
    action_set['t-'] = Action.TIME_EARLIER

    def __init__(self) -> None:
        pass


    def can_be_transferred_to(self, term: Term, full_time: bool) -> bool:
        if self.busy(term):
            return False
        elif full_time and term.is_full_time():
            return True
        elif not full_time and term.is_part_time():
            return True
        else:
            return False


    def busy(self, term: Term) -> bool:
        start_time = term.min_from_start
        end_time = term.endTime().min_from_start
        for t in Timetable.busy_set:
            if start_time in t or end_time in t:
                return True
        return False


    def put(self, lesson: Lesson) -> bool:
        if self.busy(lesson.term):
            return False
        else:
            Timetable.lesson_list.append(lesson)
            Timetable.busy_set.append(range(lesson.term.min_from_start, lesson.term.endTime().min_from_start))
            return True


    def parse(self, actions: List[str]) -> List[Action]:
        r_list = list()
        for e in actions:
            if e in Timetable.action_set.keys():
                r_list.append(Timetable.action_set[e])
        return r_list


    def perform(self, actions: List[Action]):
        assert len(actions) <= len(Timetable.lesson_list)
        for l, a in zip(Timetable.lesson_list, actions):
            if a == Action.DAY_EARLIER:
                l.earlier_day()
            elif a == Action.DAY_LATER:
                l.later_day()
            elif a == Action.TIME_LATER:
                l.later_term()
            elif a == Action.TIME_EARLIER:
                l.earlier_term()


    def get(self, term: Term) -> Lesson:
        for l in Timetable.lesson_list:
            if term == l.term:
                return l
        return None

if __name__ == '__main__':
    l1 = Lesson(Term(15, 00, day=Day.WED), "", "", 2)
    l2 = Lesson(Term(17, 00, day=Day.SAT), "", "", 2)
    l3 = Lesson(Term(18, 00, day=Day.SUN), "", "", 2)
    l4 = Lesson(Term(18, 30, day=Day.SUN), "", "", 2)
    table = Timetable()
    print(table.put(l3))
    print(table.busy_set)
    print(table.put(l4))
    print(table.busy_set)
    print(table.put(l3))
    

