#!/usr/bin/env python3
from random import randint


def main():
    pass


if __name__ == "__main__":
    main()


def calculation(num):
    checking_even = num % 2  # 1 - нечетное 0 - четное
    if checking_even == 0:
        return 'yes'
    elif checking_even == 1:
        return 'no'


rules = 'Answer "yes" if the number is even, otherwise answer "no".'

def objective():
    n = randint(1, 100)
    OP = f'{n}'
    TA = calculation(n)
    return OP, TA
