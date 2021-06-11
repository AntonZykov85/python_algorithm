from random import randint

# O(n)
def min_val(list):
    min_value = list[0]  # o(1)
    for i in list:     # O(n)
         if min_value > i: # o(1)
             min_value = i # o(1)
    return min_value

# O(n^2)
def min_val_sorted(list):
    for i in range(len(list) - 1):     # O(n)
        for j in range(len(list) - 1): # O(n)
            if list[j] > list[j + 1]:  #o(1)
                list[j] = list[j + 1]  #o(1)
    return list[0]



list = [randint(-10,25) for i in range(20)]
print(list)
print(min_val(list))
print(min_val_sorted(list))


