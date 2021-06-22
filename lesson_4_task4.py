import time
from timeit import timeit
from random import randint


array = [randint(1,100) for i in range(100**2)]

def timer(func):
    def tmp(*args, **kwargs):
        t = time.time()
        result = func(*args, **kwargs)
        print(f' время выполнения функкции {func.__name__} составило {time.time() - t}')
        return result
    return tmp

#@timer
def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


#@timer
def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'

#@timer
def func_3():
    max_3 = max([(array.count(elem), elem) for elem in set(array)])
    return f'Чаще всего встречается число {max_3[1]}, ' \
           f'оно появилось в массиве {max_3[0]} раз(а)'

print(array)
print(func_1())
print(func_2())
print(func_3())

print(f'время использования функции func_1 составлет {timeit("func_1()", number = 1, globals=globals())} секунд')
print(f'время использования функции func_2 составлет {timeit("func_2()", number = 1, globals=globals())} секунд')
print(f'время использования функции func_3 составлет {timeit("func_3()", number = 1, globals=globals())} секунд')

'''
время использования функции func_1 составлет 2.3694258 секунд
время использования функции func_2 составлет 2.345739000000001 секунд
время использования функции func_3 составлет 0.02368320000000068 секунд

ради чистоты эксперимента чуть-чуть увеличил массив. замерял время ч/з декоратор и тайм-ит, результаты сопоставимы.
как видно быстрее всего работает функция № 3(в строку), но если немного изменить код, а именно:
max_3 = max([(array.count(elem), elem) for elem in array]) - убрать set (конвертация списка в множество?), то время
выполнения функции возрастает кратно и становится сопостовимо с предложенными в домашнем задании

'''