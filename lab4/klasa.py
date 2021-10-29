class Klasa(object):

    tab = [1,2,3]

    def __init__(self, tab, v1, v2):
        print("Wywołano metodę '__init__()'")
        self.tab = tab
        self._zmienna1 = v1
        self.__zmienna2 = v2

    def __del__(self):
        print("Wywołano metodę '__del__()'")

    def __str__(self):
        return "Wywołano metodę '__str__()'"

    def __repr__(self):
        return "Wywołano metodę '__repr__()'"

    def metodaInstancyjna(self):
        print(f'Klasa.tab --> {Klasa.tab}')
        print(f'Objekt.tab --> {self.tab}')

    @classmethod
    def metodaKlasowa(cls):
        print("Wywołano metodę 'metodaKlasowa()'")

    @staticmethod
    def metodaStatyczna():
        print("Wywołano metodę 'metodaStatyczna()'")




