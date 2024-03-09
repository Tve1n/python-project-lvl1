#!/usr/bin/env python3
from random import randint, randrange


RULES = "What number is missing in the progression?"


def get_question_and_answer():
    length = 10
    start = randint(1, 21)
    step = randint(2, 5)
    end = step * length + start

    progression = list(range(start, end, step))
    hidden_index = randrange(0, length)
    answer, progression[hidden_index] = progression[hidden_index], '..'

    operation = " ".join((map(str, progression)))

    return operation, answer
