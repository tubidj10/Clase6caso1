import unittest
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from tools import get_data

class ToolTests(unittest.TestCase):
    def test_pack_rounding(self):
        self.assertEqual(get_data(ROOT,'01')['proposals'][0]['quantity'],10)
    def test_incoming_avoids_duplicate_order(self):
        self.assertEqual(get_data(ROOT,'02')['proposals'][0]['quantity'],0)
    def test_pack_rounding_second_product(self):
        self.assertEqual(get_data(ROOT,'02')['proposals'][1]['quantity'],18)
    def test_missing_lead_time_is_not_guessed(self):
        proposal=get_data(ROOT,'03')['proposals'][0]
        self.assertIsNone(proposal['quantity'])
        self.assertEqual(proposal['action'],'manual_review')
    def test_unknown_scenario_rejected(self):
        with self.assertRaises(ValueError): get_data(ROOT,'../../secret')

if __name__ == "__main__": unittest.main()
