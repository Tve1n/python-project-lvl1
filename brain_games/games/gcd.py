#!/usr/bin/env python3
from random import randint


def main():
    pass


if __name__ == "__main__":
    main()


def calculation(n1, n2):  # По алгоритму Эвклида НОД
    while n1 != n2:
        if n1 > n2:
            n1 = n1 - n2
        else:
            n2 = n2 - n1
    return n2


def objective():
        n1, n2 = randint(1, 100), randint(1, 100)
        OP = f'{n1} {n2}'
        TA = calculation(n1, n2)  # происходит операци
        return OP, TA


rules = 'Find the greatest common divisor of given numbers.'