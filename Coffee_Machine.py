from Coffee_Factory import WithMilkCoffeeFactory, WithoutMilkCoffeeFactory


class CoffeeMachine:
    def __init__(self, milk_option):
        self.milk_option = milk_option

    def making_coffee(self):
        if self.milk_option:
            print("Wybierz kawę z mlekiem: Cappuccino, LatteMachiatto")
        else:
            print("Wybierz kawę bez mleka: Espresso, Americano")

        coffee_type = input("Wybierz rodzaj kawy: ").lower()

        if self.milk_option:
            factory = WithMilkCoffeeFactory()
        else:
            factory = WithoutMilkCoffeeFactory()

        coffee = factory.create_coffee(coffee_type)
        print(f"Twoja kawa: {coffee.get_description()}")
        print(f"Cena: {coffee.get_cost()} zł")