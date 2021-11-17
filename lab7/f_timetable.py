from f_term import *
from f_lesson import *
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

    def __str__(self):

        stars = "*" * 167 + "\n"
        string = "\n"
        string += "\t\t*Poniedziałek\t\t*Wtorek\t\t\t*Środa\t\t\t*Czwartek\t\t*Piątek\t\t\t*Sobota\t\t\t*Niedziela\t\t*\n"
        string += "\t\t" + stars
        last_total = 0
        first_row = True
        lessons = self.lesson_list

        lessons.sort(key=lambda x: x.term.day)
        while len(lessons) != 0:

            count = 0
            for i in range(len(lessons)-1):
                if lessons[i].term.hour == lessons[i+1].term.hour:
                    count += 1

            same_hour_tab = [lessons[0]]
            lessons.remove(lessons[0])
            for i in range(count):
                if lessons[0].term.hour == same_hour_tab[0].term.hour:
                    same_hour_tab.append(lessons[0])
                    lessons.remove(lessons[0])
                else:
                    break

            same_hour_tab.sort(key=lambda x: x.term.day)

            total = same_hour_tab[0].term.hour * 60 + same_hour_tab[0].term.minute + same_hour_tab[0].term.duration
            hours = total // 60
            minutes = total % 60

            if not last_total == total and first_row == False:
                string += "...\t\t*\t\t\t*\t\t\t*\t\t\t*\t\t\t*\t\t\t*\t\t\t*\t\t\t*\n"
                string += "\t\t" + stars
            last_total = total
            first_row = False
            str_min_end = '0' + str(minutes) if minutes < 10 else str(minutes)
            str_min_start = '0' + str(same_hour_tab[0].term.minute) if same_hour_tab[0].term.minute < 10 else str(same_hour_tab[0].term.minute)
            string += str(same_hour_tab[0].term.hour) + ":" + str_min_start + "-" + str(hours) + ":" + str_min_end + "\t*"

            for day in range(1, 8):
                lesson_placed = False
                for element in same_hour_tab:
                    if element.term.day == Day(day):
                        if len(element.name) < 7:
                            string += element.name + "\t\t\t*"
                        else:
                            string += element.name + "\t\t*"
                        lesson_placed = True
                if lesson_placed == False:
                    string += "\t\t\t*"
            string += "\n"
            string += "\t\t" + stars

        return string

if __name__ == '__main__':

    t1 = Teacher("Stanislaw", "Polak")
    l1 = Lesson(Term(15, 00, day=Day.WED),"pp", 2, t1)
    l2 = Lesson(Term(17, 00, day=Day.SAT),"aa", 2, t1)
    l3 = Lesson(Term(18, 00, day=Day.SUN),"bb", 2, t1)
    l4 = Lesson(Term(18, 30, day=Day.THU),"cc", 2, t1)
    table = Timetable()
    table.put(l1)
    table.put(l2)
    table.put(l3)
    table.put(l4)
    print(table)
    

