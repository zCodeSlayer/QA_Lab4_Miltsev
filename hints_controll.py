# Класс для контроля используемых подсказок
class Hints(object):
    def __init__(self):
        #Создаём подсказки
        self.hint_50_50 = "50 на 50"
        self.hint_call_friend = "Звонок другу"
        self.hint_hall_help = "Помощь зала"

        #Создаём список доступных
        self.hints_list = [self.hint_50_50, self.hint_call_friend, self.hint_hall_help]

    def use_hint(self, hint_number):
        self.hints_list.pop(hint_number)

    def get_hints_count(self):
        return len(self.hints_list)