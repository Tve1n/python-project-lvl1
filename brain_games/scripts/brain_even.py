#!/usr/bin/env python3
from random import randint
import prompt


def main():
    pass

if __name__ == "__main__":
    main()


def welcome_user(name_u, game):  # !!!!!!!!! Заменить на функцию из game_logic !!!!!!!!!!!!!!!!!!!
    print("Welcome to the Brain Games!")
    print(f'Hello, {name_u}!')
    print(game)


def reaction(num):
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


def answer():       # !!!!!!!!! Заменить на функцию из game_logic !!!!!!!!!!!!!!!!!!!
    que = prompt.string("Your answer: ")  
    return que


def loop_3times():
    for i in range(3):
        n = randint(1, 100)
        print('Question: ' + str(n))
        kri = reaction(n)
        print(kri)
        if kri != cor:
            break
    else:
        print(f"Congratulations, {name_user}!")


cor = "Correct!"
name_user = prompt.string("May I have your name? ")
game_rule = 'Answer "yes" if the number is even, otherwise answer "no".'
welcome_user(name_user, game_rule)
loop_3times()
