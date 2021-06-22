from timeit import timeit
from cProfile import run

new_nums = (1234567)

def revers_1(enter_num, revers_num=0): # рекурсия О(н2)
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num

def revers_4(enter_num):
    enter_num = str(enter_num)
    revers_num = "".join(reversed(enter_num))
    return revers_num

print(f'время использования функции revers_1 составлет {timeit("revers_1(new_nums)", globals=globals())} секунд')
print(f'время использования функции revers_2 составлет {timeit("revers_2(new_nums)", globals=globals())} секунд')
print(f'время использования функции revers_3 составлет {timeit("revers_3(new_nums)", globals=globals())} секунд')
print(f'время использования функции revers_4 составлет {timeit("revers_4(new_nums)", globals=globals())} секунд')

def main():
    revers_1(new_nums)
    revers_2(new_nums)
    revers_3(new_nums)
    revers_4(new_nums)

run('main()')

#вывод: быстрее всего работает revers_3 (срез), дольше всего reverse_1 (рекурсия)