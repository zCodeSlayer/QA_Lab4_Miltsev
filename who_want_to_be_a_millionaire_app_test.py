import unittest
from who_want_to_be_a_millionaire_app import up_bank

class Test_Game_Process(unittest.TestCase):
    def test_bank(self):
        new_bank = up_bank(250)
        self.assertEqual(new_bank, 500)