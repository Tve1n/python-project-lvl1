#!/usr/bin/env python3
from random import randint


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    question = randint(1, 100)
    answer = 'no' if question % 2 > 0 else 'yes'

    return str(question), answer
