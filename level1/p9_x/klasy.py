class Lampa:
    name: str  # to są pola
    color: str  # to są pola
    fuel: int
    __log = []  # wewnętrzny ukryty log operacji

    def __init__(self, name='Starlight', color='Silver', fuel=0):
        print('uruchamiam konstuktor')
        self.name = name
        self.color = color
        self.fuel = fuel
        pass

    def __repr__(self) -> str:
        # specjalna funkcja uruchamiana gdy pojawi się potrzeba jakiegoś "wyświetlenia" klasy
        return f'Lampa(name:{self.name}, color:{self.color}, fuel:{self.fuel})'

    def add_fuel(self, how_much: int):
        print(f'dodaję fuel do lampy... {how_much}')
        self.__log_operation(f'adding {how_much} fuel to the lamp')
        # to jest metoda
        self.fuel += how_much

    def burn_fuel(self, how_much):
        print(f'lampa spala paliwo... {how_much}')
        self.fuel -= how_much

    def __log_operation(self, message):
        # "ukryta" (prywatna) operacja
        self.__log.append(message)


# tworzenie instancji klasy

l1 = Lampa(color='Gold')  # tworzenie instancji... uruchamia tzw. konstuktor
l2 = Lampa(color='Platinum')  # instancja

l1.fuel = 10
l2.fuel = 20

print(l1)
print(l2)

l1.add_fuel(2)
l2.burn_fuel(1)

print(l1)
print(l2)

