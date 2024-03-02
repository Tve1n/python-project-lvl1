#!/usr/bin/env python3
from random import randint, choice
import operator


RULES = "What is the result of the expression?"


def get_question_and_answer():
    symbols = [('+', operator.add), ('-', operator.sub), ('*', operator.mul)]
    numbers = [randint(1, 100), randint(1, 100)]
    first_number, second_number = max(numbers), min(numbers)
    operator_name, operator_method = choice(symbols)

    operation = f'{first_number} {operator_name} {second_number}'
    answer = operator_method(first_number, second_number)

    return operation, answer
