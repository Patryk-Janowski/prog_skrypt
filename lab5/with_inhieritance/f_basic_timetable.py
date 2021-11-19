from f_action import Action

class BasicTimetable:

    action_set = dict()
    action_set['d+'] = Action.DAY_LATER
    action_set['d-'] = Action.DAY_EARLIER
    action_set['t+'] = Action.TIME_LATER
    action_set['t-'] = Action.TIME_EARLIER

    def parse(self, actions):
        r_list = list()
        for e in actions:
            if e in BasicTimetable.action_set.keys():
                r_list.append(BasicTimetable.action_set[e])
            else:
                raise ValueError(f'Translation {e} is incorrect')
        return r_list

    def can_be_transferred_to(self, term, full_time: bool) -> bool:
        if self.busy_lesson(term):
            return False
        elif full_time and term.is_full_time():
            return True
        elif not full_time and term.is_part_time():
            return True
        else:
            return False