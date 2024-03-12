from abc import ABC
from homework_02.exceptions import LowFuelError,NotEnoughFuel

class Vehicle(ABC):

    def __init__(self, weight,started,fuel,fuel_consumption):
        self.weight = weight
        self.started = started
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    @property
    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
                return
        else:
            return LowFuelError()

    @property
    def move(self):
        full_need = self.weight * 0.1 * self.fuel_consumption
        if full_need <= self.fuel:
            self.fuel -= full_need
            return
        else:
            return NotEnoughFuel()





