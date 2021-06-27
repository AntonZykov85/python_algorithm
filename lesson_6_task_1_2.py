from memory_profiler import memory_usage
from timeit import default_timer
import random
from memory_profiler import profile
from random import randint


from pympler import asizeof
from sys import getsizeof

class Road:

    def __init__(self):
        self._length = float(input('введите длину дороги в метрах ', ))
        self._width = float(input('введите ширину дороги в метрах ', ))

    def mass(self):
        print('начинаем расчет массы асфальта, необходимого для покрытия всего дорожного полотна')
        return self._length * self._width * 25 * 5


class Road_1:

    __slots__ = ('_length', '_width')
    def __init__(self):
        self._length = float(input('введите длину дороги в метрах ', ))
        self._width = float(input('введите ширину дороги в метрах ', ))

    def mass(self):
        print('начинаем расчет массы асфальта, необходимого для покрытия всего дорожного полотна')
        return self._length * self._width * 25 * 5


road_1 = Road()
road_2 = Road_1()
print(asizeof.asizeof(road_1))
print(asizeof.asizeof(road_2))

'''Анализ:
задача 2 из урока 6 основ.
применение конструкции __slots__ уменьшило потребление памяти с 312 до 96
'''