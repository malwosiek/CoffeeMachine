# CoffeeMachine

Projekt Coffee to aplikacja w języku Python, która umożliwia zamawianie i tworzenie różnych rodzajów kawy. Projekt składa się z trzech głównych komponentów: klas reprezentujących rodzaje kawy, fabryk do tworzenia kawy oraz maszyny do przygotowywania kawy. Dodatkowo, w projekcie znajdują się testy jednostkowe i testy akceptacyjne.

## Struktura projektu

Projekt składa się z następujących plików:

1. `Coffee.py` - zawiera definicje klas reprezentujących różne rodzaje kawy, takie jak Espresso, Cappuccino, Americano i LatteMachiatto.

2. `Coffee_Factory.py` - zawiera fabryki do tworzenia kawy, takie jak WithoutMilkCoffeeFactory i WithMilkCoffeeFactory. Te fabryki odpowiedzialne są za tworzenie odpowiednich obiektów kawy na podstawie podanego rodzaju.

3. `Coffee_Machine.py` - zawiera klasę CoffeeMachine, która reprezentuje maszynę do przygotowywania kawy. Klasa ta obsługuje proces zamawiania kawy, tworzy odpowiednią fabrykę w zależności od opcji z mlekiem lub bez, a następnie tworzy i zwraca odpowiedni obiekt kawy.

4. `main.py` - plik główny, który inicjalizuje i uruchamia program. Pyta użytkownika o wybór opcji z mlekiem lub bez, tworzy instancję CoffeeMachine i uruchamia proces zamawiania kawy.

5. `test_coffee.py` - zawiera testy jednostkowe dla klas reprezentujących rodzaje kawy oraz fabryki do tworzenia kawy.

6. `test_acceptance.py` - zawiera testy akceptacyjne, które sprawdzają, czy program działa zgodnie z oczekiwaniami użytkownika. Testują proces zamawiania kawy z różnymi opcjami i sprawdzają poprawność wyjścia.

## Scenariusze testów

1. Testy jednostkowe (plik `test_coffee.py`):
   - Sprawdzają poprawność zwracanych opisów i kosztów dla różnych rodzajów kawy.
   - Sprawdzają, czy odpowiednie obiekty są tworzone przez fabryki.

2. Testy akceptacyjne (plik `test_acceptance.py`):
   - Testują proces zamawiania kawy z opcją z mlekiem.
   - Testują proces zamawiania kawy bez opcji z mlekiem.
   - Sprawdzają poprawność wyjścia programu dla różnych kombinacji wyborów.

## Wykorzystane narzędzia i biblioteki

Projekt Coffee został napisany w języku Python i wykorzystuje standardową bibliotekę unittest do testowania. Testy akceptacyjne wykorzystują moduł unittest.mock do symulacji wejścia i przechwycenia wyjścia programu.

## Ewentualne problemy i ich rozwiązania

Podczas pracy nad projektem mogą wystąpić pewne problemy, takie jak:
- Błędne wywołania funkcji lub metody.
- Niepoprawne opcje wyboru kawy.
- Brak obsługi nieoczekiwanych przypadków.
