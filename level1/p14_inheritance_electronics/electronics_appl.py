from level1.p14_inheritance_electronics.electronics_base import PowerSource, PoweredElement, Board


class LiIonBattery(PowerSource):
    capacity_mAh = 2500
    power_consumption_W = 0.0001
    max_current_A = 5


class Arduino(PoweredElement):
    input_voltage_range = (4.5, 5.1)
    output_voltage_range = (3.3, 5.1)
    power_consumption_W = 0.1
    max_current_A = 1


class TemperatureSensor(PoweredElement):
    input_voltage_range = (3.3, 3.3)
    output_voltage_range = (0, 0)
    power_consumption_W = 0.01
    max_current_A = 1


class StepUpVoltageRegulator(PoweredElement):
    input_voltage_range = (2, 4)
    output_voltage_range = (3, 10)
    power_consumption_W = 0.01
    max_current_A = 4


class SimpleBoard(Board):

    def __init__(self, power_source: PowerSource):
        self.power_source = power_source

    def attach(self, source: PoweredElement, drain: PoweredElement, voltage):
        source.power_drains.append(drain)
        drain.power_source = source

        # sprawdzenie czy można podłączyć tym "voltage"
        if not (source.output_voltage_range[0] <= voltage <= source.output_voltage_range[1]):
            raise RuntimeError('Wrong voltage on source')
        if not (drain.input_voltage_range[0] <= voltage <= drain.input_voltage_range[1]):
            raise RuntimeError('Wrong voltage on source')
        drain.input_voltage = voltage

    def run(self, runtime_h: float):
        power = 0
        for element in self.power_source.power_drains:
            power += element.get_current_power_W()
        power_drain_mAh = power / self.power_source.output_voltage * 1000
        self.power_source.capacity_mAh -= power_drain_mAh * runtime_h


# prosty test
battery = LiIonBattery()
board = SimpleBoard(battery)

step_up_1 = StepUpVoltageRegulator()
board.attach(battery, step_up_1, 3.7)

arduino1 = Arduino()
board.attach(step_up_1, arduino1, 5.0)

arduino2 = Arduino()
board.attach(arduino1, arduino2, 5.0)

temp1 = TemperatureSensor()
board.attach(arduino1, temp1, 3.3)

board.run(runtime_h=18.5)
print(board.power_source.capacity_mAh)
