import unittest
from hints_controll import Hints
from question import Question
from who_want_to_be_a_millionaire_app import up_bank, is_answer_right, is_hints_available

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

    def test_is_answer_right(self):
        result = is_answer_right(Question('1234',
                    ['1', '2', '3', '4'], 1), 1)
        self.assertEqual(result, True)

    def test_is_answer_false(self):
        result = is_answer_right(Question('1234',
                    ['1', '2', '3', '4'], 1), 3)
        self.assertEqual(result, False)

    def test_is_hints_available(self):
        hints = Hints()
        result = is_hints_available(hints)
        self.assertEqual(result, True)

    def test_is_hints_available_with_use_one_hint(self):
        hints = Hints()
        hints.use_hint(0, Question('1234',
                                ['1', '2', '3', '4'], 1))
        result = is_hints_available(hints)
        self.assertEqual(result, True)

    def test_is_hints_available_with_two_hints(self):
        hints = Hints()
        hints.use_hint(0, Question('1234',
                                   ['1', '2', '3', '4'], 1))
        hints.use_hint(0, Question('1234',
                                   ['1', '2', '3', '4'], 1))
        result = is_hints_available(hints)
        self.assertEqual(result, True)

    def test_is_hints_available_with_three_hints(self):
        hints = Hints()
        hints.use_hint(0, Question('1234',
                                   ['1', '2', '3', '4'], 1))
        hints.use_hint(0, Question('1234',
                                   ['1', '2', '3', '4'], 1))
        hints.use_hint(0, Question('1234',
                                   ['1', '2', '3', '4'], 1))
        result = is_hints_available(hints)
        self.assertEqual(result, False)