#!/usr/bin/env python3
from random import randint


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    number = randint(1, 100)
    operation = f'{number}'
    answer = 'no' if number % 2 > 0 else 'yes'

    return operation, answer
