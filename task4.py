def sum_numbers(n, a=1, sum_a=[]):
    if n == 0:
       print('числа в списке - ', sum_a, 'сумма чисел этих чисел равна', sum(sum_a))
    else:
        sum_a.append(a)
        a = a / -2
        n -= 1
        return sum_numbers(n, a, sum_a)

sum_numbers(5)