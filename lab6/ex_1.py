from inspect import signature

class Operacje:

    argumentySuma = [4,5]
    argumentyRoznica = [4,5,6]

    def argumenty(list_of_args):
        def decorator(original_func):
            def wrapper(self, *args):
                all_args = list(map(int, args)) + list(map(int, list_of_args))
                expected_num = len(signature(original_func).parameters)
                if len(args) > expected_num:
                    err = f'{original_func.__name__} takes exactly {expected_num} arguments ({len(args)} given)'
                    raise TypeError(err)
                retv = original_func(*all_args[:expected_num])
                if not retv and len(all_args) > expected_num:
                    return all_args[expected_num]
                else:
                    return retv
            return wrapper
        return decorator

    @argumenty(argumentySuma)
    def suma(a,b,c):
        print(f"{a}+{b}+{c}={a + b + c}")

    @argumenty(argumentyRoznica)
    def roznica(x,y):
        print(f"{x}-{y}={x - y}")

    def __setitem__(self, key, value):
            if key == 'suma':
                self.argumentySuma = value
            elif key == 'roznica':
                self.argumentyRoznica = value


op=Operacje()
op.suma(1,2,3) #Wypisze: 1+2+3=6
op.suma(1,2) #Wypisze: 1+2+4=7 - 4 jest pobierana z tablicy 'argumentySuma'
op.suma(1) #Wypisze: 1+4+5=10 - 4 i 5 są pobierane z tablicy 'argumentySuma'
try:
    op.suma() #TypeError: suma() takes exactly 3 arguments (2 given)
except TypeError:
    print('TypeError')
op.roznica(2,1) #Wypisze: 2-1=1
op.roznica(2) #Wypisze: 2-4=-2
wynik=op.roznica() #Wypisze: 4-5=-1
print(wynik) #Wypisze: 6

#Zmiana zawartości listy argumentów dekoratora  dla metody 'suma'
op['suma']=[1,2]
#oznacza, że   argumentySuma=[1,2]

#Zmiana zawartości listy argumentów dekoratora  dla metody 'roznica'
op['roznica']=[1,2,3]
#oznacza, że   argumentyRoznica=[1,2,3]