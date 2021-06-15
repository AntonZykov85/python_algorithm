def check_numbers(users_num, even_numbers=[], odd_numbers=[]):
    if users_num == 0:
        print('количество четных цифр ', len(even_numbers), '\nколичество нечетных цифр ', len(odd_numbers))
    else:
        current_num = users_num % 10
        users_num = users_num // 10
        if current_num % 2 == 0:
            even_numbers.append(current_num)
        else:
            odd_numbers.append(current_num)

        return check_numbers(users_num, even_numbers, odd_numbers)


users_num = int(input('Введите любое число не менее чем из двух знаков: '))
check_numbers(users_num)