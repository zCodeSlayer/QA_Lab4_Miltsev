# Класс для контроля используемых подсказок
import random


class Hints(object):
    def __init__(self):
        #Создаём подсказки
        self.hint_50_50 = "50 на 50"
        self.hint_call_friend = "Звонок другу"
        self.hint_hall_help = "Помощь зала"

        #Создаём список доступных
        self.hints_list = [self.hint_50_50, self.hint_call_friend, self.hint_hall_help]

    def use_hint(self, hint_number, question):
        if(self.hints_list[hint_number] == self.hint_50_50):
            answers = self.use_hint_50_50(question)
            print('Ответы 50 на 50: ', *answers)
        elif(self.hints_list[hint_number] == self.hint_call_friend):
            answer = self.use_hint_call_friend(question)
            print('Ответ друга: ', *answer)
        elif (self.hints_list[hint_number] == self.hint_hall_help):
            answer = self.use_hint_hall_help(question)
            print('Ответ зала: ', *answer)

        self.hints_list.pop(hint_number)

    def use_hint_50_50(self, question):
        random_index = random.randrange(len(question.answers_list))
        right_answer_index = question.right_answer_index
        while(right_answer_index == random_index):
            random_index = random.randrange(len(question.answers_list))
        return [question.answers_list[random_index], question.answers_list[right_answer_index]]

    def use_hint_call_friend(self, question):
        random_index = random.randrange(len(question.answers_list))
        return [question.answers_list[random_index]]

    def use_hint_hall_help(self, question):
        random_index = random.randrange(len(question.answers_list))
        return [question.answers_list[random_index]]

    def get_hints_count(self):
        return len(self.hints_list)