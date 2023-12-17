from random import randint
import prompt


def main():
    pass

if __name__ == "__main__":
    main()


def welcome_user():
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')


def answer(num):
    checking_even = num % 2  # 1 - нечетное 0 - четное
    t_again = "Let's try again, " + name + "!"
    fail = "'yes' is wrong answer ;(. Correct answer was 'no'. \n" + t_again
    f_use = question()
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


def question():
    que = prompt.string("Your answer: ")  # Ответ от пользователя
    return que


def loop_3times():
    for i in range(3):
        n = randint(1, 100)
        print('Question: ' + str(n))
        kri = answer(n)
        print(kri)
        if kri != cor:
            break
    else:
        print(f"Congratulations, {name}!")


cor = "Correct!"
name = prompt.string("May I have your name? ")
welcome_user()
loop_3times()
