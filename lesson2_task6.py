import random

def guess_number(answer = int(input('Введите число: ')), guess_num = random.randint(0, 100), counter = 10):
    print(guess_num) # вставлено для проверки работы кода. в одной из попыток написать, переменная обновлялась в каждой итерации.
    if answer == guess_num or counter == 0:
        if answer == guess_num:
            print('Поздравляю, Вы отгадали!')
        else:
            print('Пускай сегодня не повезло...попытки кончились!')
        print('Игра окончена!')
    else:
        try:
            if answer > guess_num:
                print('Ваш ответ больше загаданного! У вас осталось ', counter, 'попыток')
            if answer < guess_num:
                print('Ваш ответ меньше загаданного! У вас осталось ', counter, 'попыток')
            counter -= 1
            answer = int(input('Попробуйте еще раз: '))
            return guess_number(answer, guess_num, counter)
        except ValueError:
            print('введите число, попытка сгорела!')
            return guess_number(answer, guess_num, counter)


guess_number()
