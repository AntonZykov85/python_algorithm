from random import randint
from pympler import asizeof
from numpy import array

def func_2(nums):
    new_list = [i for i in nums if i % 2 == 0]
    return new_list

def func_2_array(nums):
    new_array = array([i for i in nums if i % 2 == 0])
    return new_array

new_nums = [i for i in range(200)]

print(asizeof.asizeof(func_2(new_nums)))
print(asizeof.asizeof(func_2_array(new_nums)))

"""Анализ:
и снова задание 1 из ДЗ № 4 в курсе основы алгоритмов.
сравниваем лист комприхэнш и нампай:
листкомпр - 4096
нампай - 520
нампай в 7 раз меньше использует память
"""
