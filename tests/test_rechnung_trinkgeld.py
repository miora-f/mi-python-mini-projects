import unittest

from pathlib import Path
import sys

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] / "01_calculators")
)

from rechnung_trinkgeld import calculate_bill

class TestRechnungTrinkgeld(unittest.TestCase):

    def test_calculate_bill(self):
        trinkgeld, gesamtbetrag, pro_person = calculate_bill(
            100, 10, 4
        )

        self.assertEqual(trinkgeld, 10)
        self.assertEqual(gesamtbetrag, 110)
        self.assertEqual(pro_person, 27.5)

if __name__ == "__main__":
    unittest.main()