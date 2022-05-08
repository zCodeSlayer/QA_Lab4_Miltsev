import unittest
from hints_controll import Hints
from question import Question

class Test_hints(unittest.TestCase):
    def test_hint_count_after_using(self):
        hints = Hints() # Создадим экземпляр класса
        count_befour_using = hints.get_hints_count() # Посчитаем кол-во подсказок до использования подсказки

        hints.use_hint(hint_number = 1) # Вызываем тестируемую функцию

        count_after_using = hints.get_hints_count() # Посчитаем кол-во подсказок после использования подсказки
        if(count_befour_using > 0):
            self.assertEqual(count_befour_using, count_after_using + 1)
        else:
            self.assertEqual(count_befour_using, count_after_using)

    def test_hint_hint_50_50(self):
        question = Question('qweasd', ['1asd', '2qwe', '3qsc', '4yhs'], 2)
        hints = Hints()
        answers = hints.use_hint_50_50(question)
        self.assertEqual(len(answers), 2)
        self.assertNotEqual(answers[0], answers[1])

    def test_hint_hint_call_friend(self):
        question = Question('qweasd', ['1asd', '2qwe', '3qsc', '4yhs'], 2)
        hints = Hints()
        answers = hints.use_hint_call_friend(question)
        self.assertEqual(len(answers), 1)


    def test_hint_hint_hall_help(self):
        question = Question('qweasd', ['1asd', '2qwe', '3qsc', '4yhs'], 2)
        hints = Hints()
        answers = hints.use_hint_call_friend(question)
        self.assertEqual(len(answers), 1)
