from abc import ABC
from homework_02.exceptions import LowFuelError,NotEnoughFuel

class Vehicle(ABC):

    def __init__(self, weight: int | float = 0, fuel: int | float = 0, fuel_consumption: int | float = 0):
        '''атрибуты weight, started, fuel, fuel_consumption со значениями по умолчанию
добавьте инициализатор для установки weight, fuel, fuel_consumption'''
        self.weight = weight
        self.started = False
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        '''метод start. При вызове этого метода необходимо проверить состояние started. И если не started, то нужно проверить, что топлива больше нуля, и обновить состояние started, иначе нужно выкинуть исключение exceptions.LowFuelError'''
        if not self.started:
            if self.fuel > 0:
                self.started = True
        else:
            raise LowFuelError()

    def move(self):
        '''метод move, который проверяет, что топлива достаточно для преодоления переданной дистанции (вплоть до полного расхода), и изменяет количество оставшегося топлива, иначе выкидывает исключение exceptions.NotEnoughFuel'''
        full_need = self.weight * 0.1 * self.fuel_consumption
        if full_need <= self.fuel:
            self.fuel -= full_need
        else:
            raise NotEnoughFuel()

