import unittest
from unittest.mock import patch
from io import StringIO
from main import main


class TestCoffeeAcceptance(unittest.TestCase):
    @patch('builtins.input', side_effect=['tak', 'cappuccino'])
    @patch('sys.stdout', new=StringIO())
    def test_acceptance_with_milk(self, mock_input, mock_output):
        expected_output = "Wybierz kawę z mlekiem: Cappuccino, LatteMachiatto\n" \
                          "Wybierz rodzaj kawy: Twoja kawa: Cappuccino\n" \
                          "Cena: 15.0 zł\n"
        main()
        self.assertEqual(mock_output.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['nie', 'espresso'])
    @patch('sys.stdout', new=StringIO())
    def test_acceptance_without_milk(self, mock_input, mock_output):
        expected_output = "Wybierz kawę bez mleka: Espresso, Americano\n" \
                          "Wybierz rodzaj kawy: Twoja kawa: Espresso\n" \
                          "Cena: 8.0 zł\n"
        main()
        self.assertEqual(mock_output.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()
