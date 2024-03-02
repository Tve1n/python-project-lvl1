#!/usr/bin/env python3
from random import randint


RULES = 'Find the greatest common divisor of given numbers.'


def get_divisor(n1, n2):  # По алгоритму Эвклида НОД
    while n1 != n2:
        if n1 > n2:
            n1 = n1 - n2
        else:
            n2 = n2 - n1
    return n2


def get_question_and_answer():
    first_num, second_num = randint(1, 100), randint(1, 100)
    operation = f'{first_num} {second_num}'
    answer = get_divisor(first_num, second_num)  # происходит операци

    return operation, answer
