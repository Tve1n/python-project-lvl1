#!/usr/bin/env python3
from random import randint


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def isEven(num):
    checking_even = num % 2  # 1 - нечетное 0 - четное
    if checking_even == 0:
        return 'yes'
    elif checking_even == 1:
        return 'no'


def getExpression():
    number = randint(1, 100)
    operation = f'{number}' #!
    answer = isEven(number) #!

    return operation, answer
