import random
import timeit
from pympler import asizeof
import copy
from statistics import median

m = int(input('введите число '))
orig_list = [random.randint(-100, 100) for i in range(2*m+1)]


# без сортировки, просто убираем минимальные значения до m и максимальные после
def mediana(array):
    for i in range((len(array)-1) // 2):
        array.remove(max(array))
        array.remove(min(array))
    return array

# пирамидальная сортировка (куча)

def HeapSort(data):
    for start in range((len(data) - 2) // 2, -1, -1):
        HeapSift(data, start, len(data) - 1)
    for end in range(len(data) - 1, 0, -1):
        data[end], data[0] = data[0], data[end]
        HeapSift(data, 0, end - 1)
    return data
def HeapSift(data, start, end):
    root = start
    while True:
        child = root * 2 + 1
        if child > end: break
        if child + 1 <= end and data[child] < data[child + 1]:
            child += 1
        if data[root] < data[child]:
            data[root], data[child] = data[child], data[root]
            root = child
        else:
            break
sorted_orig_list_1 = HeapSort(orig_list[:])

# сортировка встроеной функцией
sorted_orig_list = sorted(orig_list[:])

# встроенная медиана
mediana_1 = median(orig_list[:])


print(orig_list)
print(sorted_orig_list)
print(f' медианой является число: {sorted_orig_list[m]}')
print(f' медианой является число: {mediana(orig_list[:])}')
print(f' медианой является число: {sorted_orig_list_1[m]}')
print(f' медианой является число: {mediana_1}')

