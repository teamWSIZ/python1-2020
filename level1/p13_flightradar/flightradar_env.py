import time

from level1.p12_obiekty_2.klasy_drone import Environment, LocalizedObject


class FlightRadar24Aircraft(LocalizedObject):
    """
    Obiekt latający flightradar24.com, z danymi dostępnymi w tym systemie
    """
    ICAO_id: str
    registration_number: str


class FlightRadar24Environmet(Environment):
    """
    Środowisko skanujące obiekty latające przy pomocy flightradar24.com
    """
    min_lat: float
    max_lat: float
    min_long: float
    max_long: float

    def __init__(self, min_lat, max_lat, min_long, max_long):
        self.min_lat = min_lat
        # ........

    def scan(self):
        """
        Metoda skanująca obiekty latające "na teraz" widoczne w obszarze działania tego środowiska.
        :return:
        """
        # użyć requests by dostać dict z liniami (Listami) opisującymi samoloty
        line = ['48C986', 49.9392, 19.0193, 234, 1450, 30, '7000', 'T-EPKT143', 'B505', 'SP-TMG', 1611410572,
                '', '', '', 0, 512, 'SPTMG', 0, '']
        aircraft = self.parse_line_FR24(line)
        self.add_object(aircraft)

    def parse_line_FR24(self, line) -> FlightRadar24Aircraft:
        return FlightRadar24Aircraft()  # ... dopisać...


"""
Dane z FR24 (pojedynczy rząd):
w[0]: ICAQ id samolotu 
w[1]: szerokość geograficzna samolotu
w[2]: długość
w[3]: kurs (0 == północ, 180==południe)
w[4]: wysykość w stopach
w[5]: prędkość w 'kts' (knots == węzły)
w[9]: nr rejestracyjny
"""

if __name__ == '__main__':
    env = FlightRadar24Environmet(49, 51.1, 18, 19)
    while True:
        env.scan()
        time.sleep(15)
