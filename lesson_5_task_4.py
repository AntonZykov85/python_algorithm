from collections import OrderedDict
from timeit import timeit

my_dict = {d: d ** 2 for d in range(100**2)}
order_dict = OrderedDict(my_dict)

print(f'время выполнения .values составлет {timeit("order_dict.values()", globals=globals(), number=1000000)} секунд' )
print(f'время выполнения .values составлет {timeit("my_dict.values()", globals=globals(), number=1000000)}секунд')
print(f'время выполнения .keys составлет {timeit("order_dict.keys()", globals=globals(), number=1000000)}секунд')
print(f'время выполнения .keys составлет {timeit("my_dict.keys()", globals=globals(), number=1000000)}секунд')
print(f'время выполнения .items составлет {timeit("order_dict.items()", globals=globals(), number=1000000)}секунд')
print(f'время выполнения .items составлет {timeit("my_dict.items()", globals=globals(), number=1000000)}секунд')

"""Вывод:
время выполнения .values составлет 0.0729152 секунд
время выполнения .values составлет 0.08746010000000001секунд
время выполнения .keys составлет 0.0803856секунд
время выполнения .keys составлет 0.0886882секунд
время выполнения .items составлет 0.09478909999999996секунд
время выполнения .items составлет 0.07606270000000004секунд

Таким, образом, время выполнения операций сопоставимо, учитывая, что с 
в. 3.6 словарь упорядочен использовать орд. дикт не целесообразно"""
