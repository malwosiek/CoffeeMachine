import unittest
from Coffee import Espresso, Cappuccino, Americano, LatteMachiatto
from Coffee_Factory import WithoutMilkCoffeeFactory, WithMilkCoffeeFactory


class TestCoffee(unittest.TestCase):
    def test_espresso_description(self):
        espresso = Espresso()
        description = espresso.get_description()
        self.assertEqual(description, "Espresso")

    def test_cappuccino_cost(self):
        factory = WithMilkCoffeeFactory()
        cappuccino = factory.create_coffee("cappuccino")
        cost = cappuccino.get_cost()
        self.assertEqual(cost, 15.0)

    def test_americano_factory(self):
        factory = WithoutMilkCoffeeFactory()
        americano = factory.create_coffee("americano")
        self.assertIsInstance(americano, Americano)

    def test_latte_description_and_cost(self):
        factory = WithMilkCoffeeFactory()
        latte = factory.create_coffee("lattemachiatto")
        description = latte.get_description()
        cost = latte.get_cost()
        self.assertEqual(description, "LatteMachiatto")
        self.assertEqual(cost, 17.0)


if __name__ == "__main__":
    unittest.main()
