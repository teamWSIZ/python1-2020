from copy import copy
from typing import List

from level1.p11_symulacje_geometria_drony.vec import tangential, normalized


class Drone:
    """
    Rzeczywisty stan drona.
    """
    __pos: List[float] = [0, 0, 0]
    vel: List[float] = [0, 0, 0]
    acc: List[float] = [0, 0, -10]
    drone_axis: List[float] = [1, 0, 0]  # x == północ
    mag: List[float] = [0.71, 0, -0.71]  # trochę na północ, trochę "w dół"

    def step(self, dt: float):
        """
            Symuluje zmianę parametrów drona przy przejściu w czasie z `t` do `t+dt`.
        """
        n = len(self.__pos)
        for i in range(n):
            self.__pos[i] += self.vel[i] * dt
            self.vel[i] += self.acc[i] * dt

    def measure_gps(self):
        """
        :return: Podaje wektor położenia drona
        """
        return copy(self.__pos)

    def measure_orientation(self):
        """
        Zwraca wektor będący kierunkiem "północy". Funkcja jest OK póki przyspieszenie jest skierowane
        dokładnie w kierunku ziemi.

        :return:
        """
        return normalized(tangential(self.mag, self.acc))


def measure_magnetic(d: Drone):
    """
    :return: Jednostkowy wektor kierunku pola magnetycznego
    """
    return [0, 0, 0]


def measure_gyro(d: Drone):
    """
    :return: Prędkości kątowe wokół osi (x,y,z)
    """
    return [0, 0, 0]


if __name__ == '__main__':
    d = Drone()
    # d.acc[0] = 1
    # t = 0
    # dt = 0.001

    # while t < 1:
    #     d.step(dt)
    #     t += dt

    print(d.measure_gps())
    print(d.measure_orientation()) # sprawdzenie czy wektor pola magnetycznego jest na początku w płaszczyźnie (x,y)

    # typowe zadania:
    # napisać program który używając przśpieszeń |a|=1 dojedzie z punktu (0,0) do punktu (x,y)
    # napisać program który zmieni kierunek poruszania się drona z (1,0) do (0,1)
