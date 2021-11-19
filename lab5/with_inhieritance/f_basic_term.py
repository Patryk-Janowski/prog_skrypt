
class BasicTerm:
    
    def __init__(self, hour, minute, duration) -> None:
        self.hour = hour
        self.minute = minute
        self.duration = duration
    
    @property
    def display_min(self):
        if self.minute < 10:
            return '0' + str(self.minute)
        else:
            return str(self.minute)