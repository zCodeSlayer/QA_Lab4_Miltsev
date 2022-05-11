import unittest
from hints_controll import Hints
from question import Question
from who_want_to_be_a_millionaire_app import up_bank, game_logic

class Test_Game_Process(unittest.TestCase):
    def test_bank(self):
        new_bank = up_bank(250)
        self.assertEqual(new_bank, 500)

    def test_bank_500_to_1000(self):
        new_bank = up_bank(500)
        self.assertEqual(new_bank, 1000)

    def test_bank_1000_to_2000(self):
        new_bank = up_bank(1000)
        self.assertEqual(new_bank, 2000)

    def test_game_logic(self):
        question_list = list()
        hints = Hints()
        result = game_logic(question_list, hints)
        self.assertEqual(result, True)