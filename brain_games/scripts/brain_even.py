from random import randint
import prompt


def welcome_user():
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')


def answer(checking_even, question):
    fail = (" 'yes' is wrong answer ;(. Correct answer was 'no'. Let's try again, Bill!")
    if checking_even == 0 and question == 'yes':  # Число четное и угадал
        return "Correct!"
    elif checking_even == 0 and question == 'no':  # Число четное и не угадал
        return fail
    elif checking_even == 1 and  question == 'no':  # Число нечетное и угадал
        return "Correct"
    elif checking_even == 1 and  question == 'yes':  # Число нечетное и не угадал
        return fail
    #return checking_even != True


def question():
    que = prompt.string("Your answer: ") # Ответ от пользователя
    return que


n = randint(1, 101)
checking_even = n % 2  # 1 - нечетное 0 - четное


welcome_user()
print(n, checking_even)
print(answer(checking_even, question()))




"""
ЗАДАЧИ:
1) Рандомное число(import random)
2) Проверка числа на четность/нечетность
3) Цикл на 3 подряд вопроса
3.1) не правильный, прервать цикл break

Для начала сделать с одним числом
0 = False 
1 = True
"""