from collections import Counter, deque
from itertools import count


class HaffmanEncode:
    def __init__(self, s):
        self.s = str(s)
        self.code_table = {}


    def counter(self):
        return Counter(self.s)
        # Считаем уникальные символы.

    def haffman_tree(self):
        # Сортируем по возрастанию количества повторений.

            sorted_elements = deque(sorted(self.counter().items(), key=lambda item: item[1]))
            # Проверка, если строка состоит из одного повторяющего символа.
            if len(sorted_elements) != 1:
                # Цикл для построения дерева
                while len(sorted_elements) > 1:
                    # далее цикл объединяет два крайних левых элемента
                    # Вес объединенного элемента (накопленная частота)

                    weight = sorted_elements[0][1] + sorted_elements[1][1]
                    # Словарь из 2 крайних левых элементов, попутно вырезаем их
                    # из "sorted_elements" (из очереди).
                    # comb - объединенный элемент

                    comb = {0: sorted_elements.popleft()[0],
                            1: sorted_elements.popleft()[0]}

                    # Ищем место для ставки объединенного элемента
                    for i, _count in enumerate(sorted_elements):
                        if weight > _count[1]:
                            continue
                        else:
                            # Вставляем объединенный элемент
                            sorted_elements.insert(i, (comb, weight))
                            break
                    else:
                        # Добавляем объединенный корневой элемент после
                        # завершения работы цикла

                        sorted_elements.append((comb, weight))

            else:
                # приравниваемыем значение 0 к одному повторяющемуся символу
                weight = sorted_elements[0][1]
                comb = {0: sorted_elements.popleft()[0], 1: None}
                sorted_elements.append((comb, weight))
            return sorted_elements[0][0]

    def haffman_code(self, tree, path=''):
        # Если элемент не словарь, значит мы достигли самого символа
        # и заносим его, а так же его код в словарь (кодовую таблицу).
        if not isinstance(tree, dict):
            self.code_table[tree] = path

        # Если элемент словарь, рекурсивно спускаемся вниз
        # по первому и второму значению (левая и правая ветви).
        else:
            self.haffman_code(tree[0], path=f'{path}питон') # просто было интересно, что будет)
            self.haffman_code(tree[1], path=f'{path}алгоритм')

    def haffman_encode(self):
        # собственно сборка всего этого
        self.haffman_code(self.haffman_tree())
        return ' '.join(self.code_table[i] for i in self.s)


# строка для кодирования
new_str = (input('введите строку '))

print(f'mystery password: {HaffmanEncode(new_str).haffman_encode()}')
