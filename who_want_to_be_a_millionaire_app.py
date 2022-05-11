def up_bank(old_bank):
    return old_bank * 2

def is_answer_right(question, answer_num):
    return question.right_answer_index == answer_num

def is_hints_available(hints):
    if hints.get_hints_count() > 0:
        return True
    else:
        return False
