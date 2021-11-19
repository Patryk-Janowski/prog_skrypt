# Zdefiniuj klasę Break (przerwa pomiędzy zajęciami), która:
# posiada konstruktor Break(Term term), którego parametry określają termin przerwy oraz czas jej trwania - UWAGA: zakładamy, że przerwy odbywają w danym czasie przez wszystkie dni tygodnia, czyli pole day nie jest używane
# posiada metodę __str__() zwracającą napis "Przerwa"
# posiada metodę getTerm() zwracającą informacje nt. terminu przerwy

from f_term import Term
import f_basic_term

class Break(f_basic_term.BasicTerm):

    def __init__(self, hour, minute, duration) -> None:
        super().__init__(hour, minute, duration)
        self.term = Term(self.hour, self.minute, duration=self.duration)

    def __str__(self) -> str:
        return "Przerwa"

    def get_term(self):
        return self.term.__str__()

    