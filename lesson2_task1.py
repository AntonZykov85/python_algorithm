def calk():
    answer = input('Введите операцию(+, -, *, / или 0 для выхода) ')
    if answer == '0':
       print('программа выполнена')
    else:
        if answer in '+ - / *':
           try:
                a = int(input('введите первое число '))
                b = int(input('введите второе число '))
                if answer == '+':
                    print(a+b)
                    return calk()
                elif answer == '-':
                    print(a-b)
                    return calk()
                elif answer == '*':
                    print(a*b)
                    return calk()
                elif answer == '/':
                    print(a/b)
                    return calk()
           except ZeroDivisionError:
                print('на нуль делить нельзя!!! попробуйте еще раз')
                return calk()
        else:
            print('введите Введите операцию: +, -, *, / или 0 для выхода, а не что-то иное')
            return calk()
calk()




