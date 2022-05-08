class Question(object):
    def __init__(self, question_title, answers_list, right_answer_index):
        self.question_title = question_title
        self.answers_list = answers_list
        self.right_answer_index = right_answer_index

    def print_questions(self):
        print("Вопрос:", self.question_title)
        count = 0
        print("Выберете ответ:")
        for answer in self.answers_list:
            print(str(count) + ".", answer)