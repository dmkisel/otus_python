"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload

class Plane(Vehicle):
    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super.__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
        self.cargo = 0

    def load_cargo(self, cargo):
        if self.cargo + cargo > self.max_cargo:
            CargoOverload()
        else:
            self.cargo += cargo

    def remove_all_cargo(self):
        previous_cargo = self.cargo
        self.cargo = 0
        return previous_cargo