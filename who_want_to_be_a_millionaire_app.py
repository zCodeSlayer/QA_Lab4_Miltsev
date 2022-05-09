from question import Question
from hints_controll import Hints

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
    while(hints.get_hints_count() > 0 and hints_flag == True):
        print('Вам доступно:')
        print(*hints.hints_list, sep=', ')
        hints_str_flag = input('Желаете воспользоватся подсказками? (да/нет)')
        if(hints_str_flag == 'нет'):
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
    answer = int(input('Введите правильный ответ: '))
    if (answer != q.right_answer_index):
        print('Вы проиграли')
        break
    else:
        score = bank
        bank *= 2
