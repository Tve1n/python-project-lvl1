#!/usr/bin/env python3
from random import randint


RULES = "What number is missing in the progression?"


def getProgression():
    item = randint(1, 20)  # первое число
    list_progression = [item]
    denominator_progression = randint(2, 5)  # знаменатель прогресии

    for i in range(9):
        next_item = item + denominator_progression  # следующий элемент 
        item = next_item
        list_progression.append(next_item)

    return list_progression


def getExpression():
    spisok = getProgression()
    deleted_number = randint(0, 9)
    spisok.insert(deleted_number + 1, '..')

    answer = spisok.pop(deleted_number)
    operation = " ".join((str(x) for x in spisok))
    
    return operation, answer
