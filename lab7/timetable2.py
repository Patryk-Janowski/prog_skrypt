from f_term import *
from f_lesson import *
from typing import List
from f_action import Action
from f_break import Break

class Timetable2:

    action_set = dict()
    action_set['d+'] = Action.DAY_LATER
    action_set['d-'] = Action.DAY_EARLIER
    action_set['t+'] = Action.TIME_LATER
    action_set['t-'] = Action.TIME_EARLIER

    def __init__(self, breaks: List[Break]) -> None:
        self.lesson_list = list()
        self.busy_set = list()
        for b in breaks:
            for day in range(1,8):
                b.term.day = Day(day)
                self.put(b)


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
        for t in self.busy_set:
            if start_time in t or end_time in t:
                return True
        return False


    def put(self, lesson) -> bool:
        if self.busy(lesson.term):
            return False
        else:
            self.lesson_list.append(lesson)
            self.busy_set.append(range(lesson.term.min_from_start, lesson.term.endTime().min_from_start))
            return True


    def parse(self, actions: List[str]) -> List[Action]:
        r_list = list()
        for e in actions:
            if e in Timetable2.action_set.keys():
                r_list.append(Timetable2.action_set[e])
        return r_list


    def perform(self, actions: List[Action]):
        assert len(actions) <= len(self.lesson_list)
        for l, a in zip(self.lesson_list, actions):
            if a == Action.DAY_EARLIER:
                l.earlier_day()
            elif a == Action.DAY_LATER:
                l.later_day()
            elif a == Action.TIME_LATER:
                l.later_term()
            elif a == Action.TIME_EARLIER:
                l.earlier_term()


    def get(self, term: Term) -> Lesson:
        for l in self.lesson_list:
            if term == l.term:
                return l
        return None


if __name__ == "__main__":
    t1 = Teacher("Stanislaw", "Polak")
    l1 = Lesson(Term(15, 00, day=Day.WED),"pp", 2, t1)
    l2 = Lesson(Term(17, 00, day=Day.SAT),"aa", 2, t1)
    l3 = Lesson(Term(18, 00, day=Day.SUN),"bb", 2, t1)
    l4 = Lesson(Term(18, 30, day=Day.THU),"cc", 2, t1)
    b1 = Break(Term(9, 30, duration=15))
    b2 = Break(Term(11, 15, duration=15))
    b3 = Break(Term(12, 15, duration=15))
    b4 = Break(Term(13, 45, duration=15))
    b5 = Break(Term(14, 15, duration=15))
    b_list = [b1,b2,b3,b4,b5]
    table = Timetable2(b_list)
    table.put(l2)
    table.put(l3)
    table.put(l4)
    print(table.busy_set)