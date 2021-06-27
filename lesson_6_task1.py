from memory_profiler import memory_usage
from timeit import default_timer
import random
from memory_profiler import profile
from random import randint
import json
from pympler import asizeof
from sys import getsizeof



def memory_time(func):
    def wrapper(*args):
        t_1 = default_timer()
        mem_1 = memory_usage()[0]
        result = func(*args)
        print(f'Время выполнения функкции {func.__name__}: {default_timer() - t_1}\nПамять: {memory_usage()[0] - mem_1}')
        return result
    return wrapper

"""функция 1"""
new_nums = [i for i in range(200)]

@memory_time
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

@memory_time
def func_2(nums):
    new_list = [i for i in nums if i % 2 == 0]
    return new_list

@memory_time
def func_3(nums):
    for i in nums:
        if i % 2 == 0:
            yield i


if __name__ == "__main__":
    func_1(new_nums)
    func_2(new_nums)
    func_3(new_nums)

"""Анализ:
1) задание 1 из ДЗ № 4 в курсе основы алгоритмов.
первый вариант - цикл, второй - лист комприхэншн, третий - елд.
Время выполнения функкции func_1: 0.10461790000000001
Память: 0.015625
Время выполнения функкции func_2: 0.10785889999999998
Память: 0.0
Время выполнения функкции func_3: 0.10690630000000001
Память: 0.0
видно уменьшение снижения потребления памяти за счет л.комприх и елд.
2) 



"""