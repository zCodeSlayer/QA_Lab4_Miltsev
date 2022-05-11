import unittest

class Test_Game_Process(unittest.TestCase):
    def test_bank(self, bank):
        new_bank = up_bank(250)
        self.assertEqual(new_bank, 500)