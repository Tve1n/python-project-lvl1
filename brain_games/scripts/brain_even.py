#!/usr/bin/env python3
from random import randint
import prompt
from game_logic import *


def main():
    pass

if __name__ == "__main__":
    main()


def reaction_1(num):
    checking_even = num % 2  # 1 - нечетное 0 - четное
    t_again = "Let's try again, " + name_user + "!"
    fail = "'yes' is wrong answer ;(. Correct answer was 'no'. \n" + t_again
    f_use = answer()
    if checking_even == 0 and f_use == 'yes':  # Число четное и угадал
        return cor
    elif checking_even == 0 and f_use == 'no':  # Число четное и не угадал
        return fail
    elif checking_even == 1 and  f_use == 'no':  # Число нечетное и угадал
        return cor
    elif checking_even == 1 and  f_use == 'yes':  # Число нечетное и не угадал
        return fail
    else:
        return fail


def loop_3times():
    for i in range(3):
        n = randint(1, 100)
        print('Question: ' + str(n))
        kri = reaction_1(n)
        print(kri)
        if kri != cor:
            break
    else:
        print(f"Congratulations, {name_user}!")


game_rules = 'Answer "yes" if the number is even, otherwise answer "no".'
cor = "Correct!"
name_user = welcome_user(game_rules)

loop_3times()
