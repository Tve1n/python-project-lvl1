#!/usr/bin/env python3
from random import randint

def main():
    pass


if __name__ == "__main__":
    main()


def IsPrime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n


def calculation(num):
    checking_prime = IsPrime(num)
    if checking_prime is True:
        return "yes"
    elif checking_prime is False:
        return "no"


def objective():
    n = randint(5, 50)
    OP = f'{n}'
    TA = calculation(n)
    return OP, TA


rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'

