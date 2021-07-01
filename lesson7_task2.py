import operator
import random
import timeit
from pympler import asizeof



def merge_sort(L, compare=operator.lt):
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L) / 2)
        left = merge_sort(L[:middle], compare)
        right = merge_sort(L[middle:], compare)
        return merge(left, right, compare)

def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

orig_list_1 = [random.randint(0, 50) for i in range(100)]
orig_list_2 = [random.randint(0, 50) for i in range(1000)]
orig_list_3 = [random.randint(0, 50) for i in range(10000)]

print(f' first array: {orig_list_1} '
      f'\n second array:{orig_list_2} '
      f'\n trith array: {orig_list_3}')

print(f' first sorted array: {merge_sort(orig_list_1)} '
      f'\n second sorted  array:{merge_sort(orig_list_2)} '
      f'\n trith sorted array: {merge_sort(orig_list_3)}')

print(f' сортировка массива длиной {len(orig_list_1)} выполняется за '
      f'{timeit.timeit("merge_sort(orig_list_1[:])", globals=globals(), number=1000)} секунд '
      f'и занимает {asizeof.asizeof(merge_sort(orig_list_1))} памяти')

print(f' сортировка массива длиной {len(orig_list_2)} выполняется за '
      f'{timeit.timeit("merge_sort(orig_list_2[:])", globals=globals(), number=1000)} секунд '
      f'и занимает {asizeof.asizeof(merge_sort(orig_list_2))} памяти')

print(f' сортировка массива длиной {len(orig_list_3)} выполняется за '
      f'{timeit.timeit("merge_sort(orig_list_3[:])", globals=globals(), number=1000)} секунд '
      f'и занимает {asizeof.asizeof(merge_sort(orig_list_3))} памяти')

"""Вывод:
 сортировка массива длиной 100 выполняется за 0.3121654 секунд и занимает 2368 памяти
 сортировка массива длиной 1000 выполняется за 3.9033364999999995 секунд и занимает 10640 памяти
 сортировка массива длиной 10000 выполняется за 49.61644939999999 секунд и занимает 89240 памяти
 
 аналогичный массив (0;50 in range(10000) пузырьком:
  сортировка массива длиной 10000 выполняется за 921.6307005 секунд и занимает 81680 памяти
т.е. чуть менее затратно по памяти но намного дольше
  
"""