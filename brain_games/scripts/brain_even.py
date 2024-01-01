#!/usr/bin/env python3
from random import randint
from brain_games.scripts.game_logic import welcome_user, \
    answer, reaction


def main():
    pass


if __name__ == "__main__":
    main()


def reaction_1(num, f_use):
    checking_even = num % 2  # 1 - нечетное 0 - четное
    if checking_even == 0 and f_use == 'yes':  # Число четное и угадал
        return True
    elif checking_even == 0 and f_use == 'no':  # Число четное и не угадал
        return False
    elif checking_even == 1 and f_use == 'no':  # Число нечетное и угадал
        return True
    elif checking_even == 1 and f_use == 'yes':  # Число нечетное и не угадал
        return False
    else:
        return False


def loop_3times():
    for i in range(3):
        n = randint(1, 100)
        print(f'Question: {n}')
        guess = answer()
        check = reaction_1(n, guess)
        if check is True:
            print(cor)
            continue
        elif check is False:
            if guess == 'yes':
                rev = 'no'
            elif guess == 'no':
                rev = 'yes'
            print(reaction(name_user, guess, rev))
            break
    else:
        print(f"Congratulations, {name_user}!")


game_rules = 'Answer "yes" if the number is even, otherwise answer "no".'
cor = "Correct!"
name_user = welcome_user(game_rules)

loop_3times()
