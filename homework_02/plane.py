"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload

class Plane(Vehicle):
    def __init__(self, weight: int | float = 0, fuel: int | float = 0, fuel_consumption: int | float = 0, max_cargo: int = 0):
        super.__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
        self.cargo = 0
    def load_cargo(self, cargo):
        if self.cargo + cargo > self.max_cargo:
            raise CargoOverload()
        else:
            self.cargo += cargo

    def remove_all_cargo(self) -> int | float:
        previous_cargo = self.cargo
        self.cargo = 0
        return previous_cargo