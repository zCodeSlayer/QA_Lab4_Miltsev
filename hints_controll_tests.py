import unittest
from hints_controll import Hints

class Test_hints(unittest.TestCase):
    def test_hint_count_after_using(self):
        hints = Hints() # Создадим экземпляр класса
        count_befour_using = hints.get_hints_count() # Посчитаем кол-во подсказок до использования подсказки

        hints.use_hint() # Вызываем тестируемую функцию

        count_after_using = hints.get_hints_count() # Посчитаем кол-во подсказок после использования подсказки
        if(count_befour_using > 0):
            self.assertEqual(count_befour_using, count_after_using + 1)
        else:
            self.assertEqual(count_befour_using, count_after_using)