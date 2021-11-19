from re import T
from unittest import case
from f_term import *
from f_lesson import *
from typing import List
from f_action import Action
from f_break import Break
from copy import copy

class Timetable2:

    action_set = dict()
    action_set['d+'] = Action.DAY_LATER
    action_set['d-'] = Action.DAY_EARLIER
    action_set['t+'] = Action.TIME_LATER
    action_set['t-'] = Action.TIME_EARLIER
    skip_break = False

    def __init__(self, breaks: List[Break]) -> None:
        self.lesson_list = list()
        self.lesson_set = list()
        self.break_set = list()
        for b in breaks:
            for day in range(1,8):
                b.term.bre = True
                b.term.day = Day(day)
                self.put_break(b)


    def can_be_transferred_to(self, term: Term, full_time: bool) -> bool:
        if self.busy_lesson(term):
            return False
        elif full_time and term.is_full_time():
            return True
        elif not full_time and term.is_part_time():
            return True
        else:
            return False


    def busy_lesson(self, term: Term) -> bool:
        start_time = term.min_from_start + 1
        end_time = term.endTime().min_from_start - 1
        for t in self.lesson_set:
            if start_time in t or end_time in t:
                return True
        return False

    def busy_break(self, term: Term) -> bool:
        start_time = term.min_from_start + 1
        end_time = term.endTime().min_from_start - 1
        for t in self.break_set:
            if start_time in t or end_time in t:
                return True
        return False


    def busy(self, term: Term):
        if self.busy_lesson(term) or self.busy_break(term):
            return True
        else:
            return False


    def put(self, lesson) -> bool:
        if self.busy_lesson(lesson.term) or self.busy_break(lesson.term):
            return False
        else:
            self.lesson_list.append(lesson)
            self.lesson_set.append(range(lesson.term.min_from_start, lesson.term.endTime().min_from_start))
            return True


    def put_break(self, bre) -> bool:
        if self.busy_lesson(bre.term) or self.busy_break(bre.term):
            return False
        else:
            self.break_set.append(range(bre.term.min_from_start, bre.term.endTime().min_from_start))
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
                self.earlier_day(l)
            elif a == Action.DAY_LATER:
                self.later_day(l)
            elif a == Action.TIME_LATER:
                self.later_term(l)
            elif a == Action.TIME_EARLIER:
                self.earlier_term(l)


    def later_day(self, lesson: Lesson):
        lesson.later_day()

    def earlier_day(self, lesson: Lesson):
        lesson.earlier_day() 

    def later_term(self, lesson):
        self.move(lesson, 'lt')  

    def earlier_term(self, lesson):
        self.move(lesson, 'et')  



    def move(self, lesson, func):
        new_lesson = copy(lesson)
        if func == 'lt':
            new_lesson.later_term()
        elif func == 'et':
            new_lesson.earlier_term()
        if not self.busy_break(new_lesson.term) and not self.busy_lesson(new_lesson.term):
            lesson.term = new_lesson.term
        elif self.skip_break and self.busy_break(new_lesson.term):
            ra_break = self.get_range_break(new_lesson.term)
            if func == 'et':
                new_lesson.term = new_lesson.term.min_to_instance(ra_break[0] - new_lesson.term.duration, new_lesson.term.duration)
            elif func == 'lt':
                new_lesson.term = new_lesson.term.min_to_instance(ra_break[-1] + 1, new_lesson.term.duration)
            ra_lesson = self.get_range_lesson(lesson.term)
            if ra_lesson:
                self.lesson_set.remove(ra_lesson)
            if not self.busy_lesson(new_lesson.term):
                lesson.term = new_lesson.term
    



    def get(self, term: Term) -> Lesson:
        for l in self.lesson_list:
            if term == l.term:
                return l
        return None


    def get_range_break(self, term):
        start_time = term.min_from_start + 1
        end_time = term.endTime().min_from_start - 1
        for t in self.break_set:
            if start_time in t or end_time in t:
                return t
        return None

    def get_range_lesson(self, term):
        start_time = term.min_from_start + 1
        end_time = term.endTime().min_from_start - 1
        for t in self.lesson_set:
            if start_time in t or end_time in t:
                return t
        return None
        



if __name__ == "__main__":
    t1 = Teacher("Stanislaw", "Polak")
    l1 = Lesson(Term(8, 00, day=Day.MON),"pp", 2, t1)
    b1 = Break(Term(9, 30, duration=15))
    b2 = Break(Term(11, 15, duration=15))
    b_list = [b1, b2]
    table = Timetable2(b_list)
    Timetable2.skip_break = True
    table.put(l1)

    print(l1)

    table.later_term(l1)
    print(l1.term)

    table.later_term(l1)
    print(l1.term)
    
    table.earlier_term(l1)
    print(l1.term)
    
    table.earlier_term(l1)
    print(l1.term)

    table.skip_break = False
    table.later_term(l1)
    print(l1.term)

    