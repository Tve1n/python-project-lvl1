#!/usr/bin/env python3
from random import randint


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    d = 2
    while d * d <= num and num % d != 0:
        d += 1
    return d * d > num > 1


def get_question_and_answer():
    question = randint(5, 50)
    if is_prime(question):
        answer = 'yes'
    else:
        answer = "no"

    return str(question), answer
