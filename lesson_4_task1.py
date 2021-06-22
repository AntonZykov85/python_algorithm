from timeit import timeit

new_nums = [i for i in range(200)]

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

def func_2(nums):
    new_list = [i for i in nums if i % 2 == 0]
    return new_list

print(f'время использования функции func_1 составлет {timeit("func_1(new_nums)", globals=globals())} секунд')
print(f'время использования функции func_2 составлет {timeit("func_2(new_nums)", globals=globals())} секунд')

# ИТОГО: использование л.компрех-шн на текушей машине ~30% быстрее ф-ции, сформированной через цикл цикл фор.