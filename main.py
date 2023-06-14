from abc import ABC, abstractmethod
from Coffee_Machine import CoffeeMachine


def main():
    milk_option = input("Czy chcesz kawę z mlekiem? (tak/nie): ")
    if milk_option.lower() == 'tak':
        milk_option = True
    else:
        milk_option = False

    coffee_machine = CoffeeMachine(milk_option)
    coffee_machine.making_coffee()

if __name__ == "__main__":
    main()
