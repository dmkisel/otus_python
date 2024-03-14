"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.engine import Engine

class Car(Vehicle):
    def __init__(self, engine):
        self.engine = None

    def set_engine(self, engine):
        self.engine = Engine
