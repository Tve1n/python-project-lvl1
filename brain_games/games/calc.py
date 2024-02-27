#!/usr/bin/env python3
from random import randint, choice
import operator


RULES = "What is the result of the expression?"


def getExpression():
    spisok = [('+', operator.add), ('-', operator.sub), ('*', operator.mul)]
    numbers = [randint(1, 100), randint(1, 100)]
    first_number, second_number = max(numbers), min(numbers)
    znak = choice(spisok)

    operation = f'{first_number} {znak[0]} {second_number}'
    answer = znak[1](first_number, second_number)

    return operation, answer
