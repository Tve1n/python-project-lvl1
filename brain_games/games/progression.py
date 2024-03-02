#!/usr/bin/env python3
from random import randint


RULES = "What number is missing in the progression?"


def get_question_and_answer():
    lenght_list = 10
    first_num = randint(1, 21)
    denominator_progression = randint(2, 5)  # шаг прогрессии
    last_num = denominator_progression * lenght_list + first_num + 1

    list_progression = list(range(first_num, last_num, denominator_progression))
    deleted_number = randint(0, 9)
    list_progression.insert(deleted_number + 1, '..')

    answer = list_progression.pop(deleted_number)
    operation = " ".join((str(x) for x in list_progression))

    return operation, answer
