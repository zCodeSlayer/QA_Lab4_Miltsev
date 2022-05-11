from hints_controll import Hints
from question import Question

def up_bank(old_bank):
    return old_bank * 2

def is_answer_right(question, answer_num):
    return question.right_answer_index == answer_num

def is_hints_available(hints):
    if hints.get_hints_count() > 0:
        return True
    else:
        return False

if __name__ == '__main__':
    question_list = list()
    hints = Hints()
    bank = 250
    score = 0

    question_list.append(Question('Белый медвежёнок, который ищет друга',
                                  ['Чупакабра', 'Умка', 'Чебурашка', 'Чунга-Чанга'], 1))
    question_list.append(Question('Какую площадь имеет клетка стандартной школьной тетради',
                                  ['0,25 кв. см.', '0,5 кв. см.', '1 кв. см.', '1,25 кв. см.'], 0))

    for q in question_list:
        print('Ваш банк ' + str(score) + ' рублей')
        q.print_questions()
        hints_flag = True
        while (is_hints_available(hints) and hints_flag == True):
            print('Вам доступно:')
            print(*hints.hints_list, sep=', ')
            hints_str_flag = input('Желаете воспользоватся подсказками? (да/нет)')
            if (hints_str_flag == 'нет'):
                hints_flag = False
                break
            else:
                print('Выберете подсказку: ')
                count = 0
                for hint in hints.hints_list:
                    print(str(count) + '. ' + hint)
                    count += 1
                hint_num = int(input('Введите номер подсказки: '))
                hints.use_hint(hint_num, q)
        answer_res = is_answer_right(q, int(input('Введите правильный ответ: ')))
        if (answer_res == False):
            print('Вы проиграли')
            break
        else:
            score = bank
            bank = up_bank(bank)
