import timeit
import random
from pympler import asizeof


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_mod(lst_obj):
    n = 1
    trigger = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                trigger = 0
            if trigger == 1:
                break
        n += 1
    return lst_obj

orig_list = [random.randint(0, 50) for _ in range(10000)]
sorted_list = [i for i in range(1000)]
#print(sorted_list)
#print(orig_list)
#print(f' сортированный список оригинальный массив {bubble_sort(orig_list)}')
#print(f' сортированный список сортированный массив {bubble_sort(sorted_list)}')
#print(f' сортированный модифицированный список оригинальный массив {bubble_sort_mod(orig_list)}')
#print(f' сортированный модифицированный список сортированный массив {bubble_sort_mod(sorted_list)}')

#print(bubble_sort(orig_list))

# замеры 1000
print(f' сортировка массива длиной {len(orig_list)} выполняется за '
      f'{timeit.timeit("bubble_sort(orig_list[:])", globals=globals(), number=100)} секунд '
      f'и занимает {asizeof.asizeof(bubble_sort(orig_list[:]))} памяти')

print(f' сортировка заранее отсортированного массива длиной {len(sorted_list)} выполняется за '
      f'{timeit.timeit("bubble_sort(sorted_list[:])", globals=globals(), number=100)} секунд '
      f'и занимает {asizeof.asizeof(bubble_sort(sorted_list))} памяти')

print(f' сортировка массива длиной {len(orig_list)} модифицированным скриптом выполняется за '
      f'{timeit.timeit("bubble_sort_mod(orig_list[:])", globals=globals(), number=100)} секунд '
      f'и занимает {asizeof.asizeof(bubble_sort_mod(orig_list))} памяти')

print(f' сортировка заранее отсортированного массива длиной {len(sorted_list)} модифицированным скриптом '
      f'выполняется за {timeit.timeit("bubble_sort_mod(sorted_list[:])", globals=globals(), number=100)} секунд '
      f'и занимает {asizeof.asizeof(bubble_sort_mod(sorted_list))} памяти')

"""Вывод:
 - сортировка массива длиной 100 выполняется за 0.43711030000000006 секунди занимает 3728 памяти;
 - сортировка заранее отсортированного массива длиной 100 выполняется 
 за 0.40309209999999995 секунди занимает 4048 памяти;
 - сортировка массива длиной 100 модифицированным скриптом выполняется 
 за 0.08097290000000013 секунди занимает 3728 памяти;
 - сортировка заранее отсортированного массива длиной 100 модифицированным скриптомвыполняется 
 за 0.04814040000000008 секунди занимает 4048 памяти;
 
 
- сортировка массива длиной 1000 выполняется за 9.9252439 секунд и занимает 26032 памяти;
- сортировка заранее отсортированного массива длиной 1000 
выполняется за 12.145956300000002 секунд и занимает 41008 памяти;
- сортировка массива длиной 1000 модифицированным скриптом 
выполняется за 9.246497000000002 секунд и занимает 26992 памяти;
- сортировка заранее отсортированного массива длиной 1000 модифицированным скриптом
 выполняется за 0.06836200000000048 секунд и занимает 41008 памяти;
 
 Таким образом, модифицированный скрипт сортировки работает с заранее сортированным списком на порядок быстрее.
 Кроме того, в ряде замеров (я их сделал около 10-15) он достаточно быстро отработал и с несортированным, 
 видимо Великий Рандом выдал +/- отсортированный список"""


