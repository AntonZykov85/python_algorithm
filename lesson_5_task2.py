a = list('A2')
b = list('C4F')
summ = list(hex(int(''.join(a), 16) + int(''.join(b), 16)))
mult = list(hex(int(''.join(a), 16) * int(''.join(b), 16)))
print(f'Сумма чисел равна: {summ[2:]}')
print(f'Произведение чисел равно: {mult[2:]}')
