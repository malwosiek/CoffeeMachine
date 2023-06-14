from abc import ABC, abstractmethod
from Coffee import Espresso, Cappuccino, Americano, LatteMachiatto

class MilkCoffeeFactory(ABC):
    @abstractmethod
    def create_coffee(self):
        pass

class WithoutMilkCoffeeFactory(MilkCoffeeFactory):
    def create_coffee(self, coffee_type):
        if coffee_type == "espresso":
            return Espresso()
        elif coffee_type == "americano":
            return Americano()
        else:
            raise ValueError("Niepoprawny rodzaj kawy")

class WithMilkCoffeeFactory(MilkCoffeeFactory):
    def create_coffee(self, coffee_type):
        if coffee_type == "cappuccino":
            return Cappuccino()
        elif coffee_type == "lattemachiatto":
            return LatteMachiatto()
        else:
            raise ValueError("Niepoprawny rodzaj kawy")