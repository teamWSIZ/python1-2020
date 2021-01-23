from math import sqrt
from typing import List


class PhysicalObject:
    """
    Obiekty tej klasy mogą być symulowane, tzn. mają funkcję która mówi jak zmeinia się ich stan
    przy przejściu w czasie z t -> t+dt
    """

    def step(self, t, dt):
        pass


class LocalizedObject(PhysicalObject):
    """
    Obiekty tej klasy posiadają pozycję, i prędkość która mówi o zmianie tej pozycji w czasie.
    Klasa rozszerza (extends) typ PhysicalObject
    """
    position: List[float]
    velocity: List[float]


class Drone(LocalizedObject):
    """
    Specjalna klasa odpowiadająca za dron (z danymi które _on_ widzi)
    """

    def get_velocity_magnitude(self):
        vel = sqrt(sum([v ** 2 for v in self.velocity]))
        return vel


class Airplane(LocalizedObject):
    """
    Specjalna klasa odpowiadająca za zarejestrowany samolot
    """
    registration: str
    aircraft_type: str

    def __init__(self, registration_number: str):
        self.registration = registration_number


class Environment:
    flying_objects: List[LocalizedObject] = []

    def add_object(self, p: LocalizedObject):
        self.flying_objects.append(p)

    def simulate(self, t0, t1, dt):
        """
        Symuluje zachowanie wszystkich obiektów środowiska od t0 do t1 z krokiem czasowym dt
        """
        t = t0
        while t <= t1:
            print('----')
            for p in self.flying_objects:
                p.step(t, dt)
                print(p.position)
            t += dt




if __name__ == '__main__':
    d = Drone()
    d.position = [1, 2, 3]
    print(d.position)
    ap = Airplane('TC-JJL')
    ap.position = [51.1402, 18.7028, 37000]
    print(ap.registration)

    visible_objects: List[LocalizedObject]
    visible_objects = [d, ap]  # w liście udało się umieścić obiekty różnych klas, ale mające wspólnego "przodka"

    print('--------')
    for o in visible_objects:
        print(f'x={o.position[0]}    y={o.position[1]}')
