#!/usr/bin/env python3
from random import randint


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def isPrime(num):
    d = 2
    while d * d <= num and num % d != 0:
        d += 1
    if d * d > num:
        return "yes"
    else:
        return "no"


def getExpression():
    number = randint(5, 50)
    operation = f'{number}' #!
    answer = isPrime(number) #! Поменять имя переменных

    return operation, answer
