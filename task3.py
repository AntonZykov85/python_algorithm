
def reverse_numbers(users_num, reverse_num=[]):
    if users_num == 0:
        print(''.join(map(str, reverse_num)))
    else:
        current_num = users_num % 10
        users_num = users_num // 10
        reverse_num.append(current_num)
        return reverse_numbers(users_num, reverse_num)


users_num = int(input('Введите любое число не менее чем из двух знаков: '))
reverse_numbers(users_num)