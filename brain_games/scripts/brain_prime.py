#!/usr/bin/env python3
from random import randint
from brain_games.scripts.game_logic import welcome_user, \
    answer, reaction


def main():
    pass


if __name__ == "__main__":
    main()


def IsPrime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n


def operation(num, ans):
    checking_prime = IsPrime(num)
    if checking_prime is True and ans == 'yes':  # Число четное и угадал
        return True
    elif checking_prime is False and ans == 'no':  # Число четное и не угадал
        return True
    elif checking_prime is True and ans == 'no':  # Число нечетное и угадал
        return False
    elif checking_prime is False and ans == 'yes':  # Число нечетное и не угадал
        return False
    else:
        return False


def loop():
    for i in range(3):
        rand_num = randint(5, 50)

        print(f'Question: {rand_num}')  # задается вопрос пользователю

        guess = answer()  # ответ от пользователя
        check = operation(rand_num, guess)  # Проверка на правильность ответа
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


game_rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
cor = "Correct!"
name_user = welcome_user(game_rules)

loop()
