from abc import abstractmethod, ABC


class Coffee(ABC):
    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass

class Espresso(Coffee):
    def get_description(self):
        return "Espresso"

    def get_cost(self):
        return 8.0

class Cappuccino(Coffee):
    def get_description(self):
        return "Cappuccino"

    def get_cost(self):
        return 15.0

class Americano(Coffee):
    def get_description(self):
        return "Americano"

    def get_cost(self):
        return 10.00

class LatteMachiatto(Coffee):
    def get_description(self):
        return "LatteMachiatto"

    def get_cost(self):
        return 17.00
