from collections import deque
from random import randint
import time


array = [randint(1,100) for i in range(100**4)]
deque_array = deque(array)

def timer(func):
    def tmp(*args, **kwargs):
        t = time.time()
        result = func(*args, **kwargs)
        print(f' время выполнения функкции {func.__name__} составило {time.time() - t}')
        return result
    return tmp

@timer
def list_insert(lst, num):
    for i in range(num):
        lst.insert(0, i)
    #return lst

@timer
def list_pop(lst, num):
    for i in range(num):
        lst.pop(0)
   # return lst

@timer
def list_extend(lst):
    lst.reverse()
    lst.extend([randint(1,100) for i in range(20)][::-1])
    lst.reverse()
  #  return lst

@timer
def deque_appendleft(deque_lst, num):
    for i in range(num):
        deque_lst.appendleft(i)
   # return deque_lst

@timer
def deque_popleft(deque_lst, num):
    for i in range(num):
        deque_lst.popleft()
   # return deque_lst

@timer
def deque_extendleft(deque_lst):
    deque_lst.extendleft([randint(1,100) for i in range(20)])
   # return deque_lst

if __name__ == '__main__':
    list_insert(array, 7)
    deque_appendleft(deque_array, 7)
    list_extend(array)
    deque_extendleft(deque_array)
    list_pop(array, 7)
    deque_popleft(deque_array, 7)

"""Выводы:
 замеры при размере массива 100**4:
 время выполнения функкции list_insert составило 0.6520068645477295
 время выполнения функкции deque_appendleft составило 0.0
 время выполнения функкции list_extend составило 0.16068172454833984
 время выполнения функкции deque_extendleft составило 0.0
 время выполнения функкции list_pop составило 0.5965347290039062
 время выполнения функкции deque_popleft составило 0.0
 как говорится результат на лицо. очередь кратно быстрее чем список, если работать с началом списка """

