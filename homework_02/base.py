from abc import ABC
from homework_02.exceptions import LowFuelError,NotEnoughFuel

class Vehicle(ABC):

    def __init__(self, weight=0, fuel=0, fuel_consumption=0):
        self.weight = weight
        self.started = False
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
        else:
            LowFuelError()

    @property
    def move(self):
        full_need = self.weight * 0.1 * self.fuel_consumption
        if full_need <= self.fuel:
            self.fuel -= full_need
        else:
            NotEnoughFuel()





