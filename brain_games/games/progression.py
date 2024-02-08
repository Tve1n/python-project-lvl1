#!/usr/bin/env python3
from random import randint


def main():
    pass


if __name__ == "__main__":
    main()


def progression():
    b_prev = randint(1, 20)  # первое число
    list_progress = [b_prev]
    q = randint(2, 5)  # знаменатель прогресии
    for i in range(9):
        b_cur = b_prev + q  # следующий элемент прогрессии
        b_prev = b_cur
        list_progress.append(b_cur)
    return list_progress


def objective():
    spisok = progression()
    rand_num = randint(0, 9)
    spisok.insert(rand_num + 1, '..')
    TA = spisok.pop(rand_num)  # Удаленное из последовательности число
    OP = " ".join((str(x) for x in spisok))
    return OP, TA


rules = "What number is missing in the progression?"
