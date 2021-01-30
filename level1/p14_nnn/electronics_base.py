from typing import List


# declarations
class PowerSource:
    pass


class PoweredElement:
    pass


class Board:
    pass


## proper system

class PoweredElement:
    input_voltage_range = (0, 100)
    input_voltage = 10
    output_voltage_range = (0, 100)
    power_consumption_W = 1
    max_current_A = 2

    power_source: PoweredElement
    power_drains: List[PoweredElement]

    def __init__(self) -> None:
        self.power_drains = []

    def get_current_power_W(self) -> float:
        """
        Power drained by this element, and all elements connected to it (power_drains);
        Note:
            - this power should not exceed max_current_A
            - the drains themselves must also calculate the power drained by their drains
        """
        power = self.power_consumption_W
        for element in self.power_drains:
            power += element.get_current_power_W()
        return power


class PowerSource(PoweredElement):
    """
    Klasa "dziedziczy" z PoweredElement, tzn. posiada wszystkie pola i metody tamtej klasy
    (choć może je nadpisać)... oraz dodatkowo wszystko co tu jest zadeklarowane.
    """
    output_voltage_range = (3.7, 3.7)  # nadpisuje wartości z PoweredElement
    output_voltage = 3.7
    capacity_mAh = 2000


class Board:
    """
    Klasa służąca do symulacji całego układu
    """
    power_source: PowerSource

    def attach(self, source: PoweredElement, drain: PoweredElement, voltage):
        """
        Podłącza elementy tak, by prąd dla `drain` był podawany przez `source`.
        :param voltage -- podaje jakim dokładnie napięciem podłączono elementy
        """
        pass

    def validate(self, runtime_h: float):
        """
        Sprawdza czy cały układ jest ułożony OK, tzn. czy nie zostały przekroczone parametry max_current,
        czy odpowiednio są ustawione voltage itp.
        :param: runtime_h -- czas przez który układ ma działać; liczba w godzinach
        :return: True jeśli układ jest OK, i power_source nie wyładuje się w ciągu runtime_h.
        """
        pass

    def run(self, runtime_h: float):
        pass