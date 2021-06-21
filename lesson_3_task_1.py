import time
new_list = []
new_dict = {}
n = 10 ** 7

def timer(func):
    def tmp(*args, **kwargs):
        t = time.time()
        result = func(*args, **kwargs)
        print(f'время выполнения функции {func.__name__} составило: {time.time()-t}')
        return result
    return tmp

@timer
def list_append(lst, num):
    for i in range(num):
        lst.append(i)
        return lst

@timer
def list_change(lst):
    for i in range(len(lst)):
        lst[i] = '1qwe67!!'
    return lst

@timer
def list_pop(lst, n):
    for i in range(n):
        lst.pop(i)
        return lst

@timer
def dict_append(dct, n):
    for i in range(n):
        dct[i] = i
        return dct

@timer
def dict_pop(dct, n):
    for i in range(n):
        dct.pop(i)
        return dct

@timer
def dict_change(dct, n):
    for i in range(n):
        dct[i] = '1qwe67!!'
    return dct

@timer
def new_list_append(n):
    return [el for el in range(n)]

@timer
def new_dict_append(n):
    return {el for el in range(n)}


if __name__ == '__main__':
    list_append(new_list, n) # 0.0 - сложность O(1) - константа
    list_change(new_list) # 0.0 - сложность O(1) - константа
    list_pop(new_list, n) # 0.0 - сложность О(n) - линейная для списков
    dict_append(new_dict, n) # 0.0 - сложность O(1)
    dict_change(new_dict, n) # 0,78106522 - сложность O(1), видимо на слабеньком ноуте подгружает память
    dict_pop(new_dict, n) # 0.0 - сложность O(1)
    new_dict_append(n) # 0.499 - сложность O(n)
    new_list_append(n) # 0,484 - сложность O(n)



