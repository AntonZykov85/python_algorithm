def sum_numbers(n, start_number=1, list_numb=[]):
    if n == 0:
       print('числа в списке - ', list_numb, 'сумма чисел этих чисел равна', sum(list_numb))
    else:
        list_numb.append(start_number)
        start_number = start_number / -2
        n -= 1
        return sum_numbers(n, start_number, list_numb)


n = int(input('введите количество цифр для расчета '))

sum_numbers(n)
