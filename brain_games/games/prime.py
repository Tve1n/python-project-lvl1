#!/usr/bin/env python3
from random import randint


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def check_prime(num):
    d = 2
    while d * d <= num and num % d != 0:
        d += 1
    if d * d > num > 1:
        return "yes"
    else:
        return "no"


def get_question_and_answer():
    number = randint(5, 50)
    operation = f'{number}'
    answer = check_prime(number)

    return operation, answer
