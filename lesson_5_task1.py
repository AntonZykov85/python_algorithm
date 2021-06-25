from collections import namedtuple

firm_tuple = namedtuple('firm_tuple', 'firm_name qr_1 qr_2 qr_3 qr_4')
count = int(input('введите количество организаций: '))
firm_profit = {}
max_firm = []
min_firm = []

for i in range(count):
    firm = firm_tuple(input('введите наименование организации: '),
                      int(input('введите размер прибыли за 1 кв: ')), #здесь должен быть трай - эксепт для обхода ошибки ввода символов
                      int(input('введите размер прибыли за 2 кв: ')),
                      int(input('введите размер прибыли за 3 кв: ')),
                      int(input('введите размер прибыли за 4 кв: ')))
    firm_profit[firm.firm_name] = firm.qr_1 + firm.qr_2 + firm.qr_3 + firm.qr_4

average_profit = sum(firm_profit.values())/count

for k, v in firm_profit.items():
    if v < average_profit:
        min_firm.append(k)
    else:
        max_firm.append(k)

print(f'прибыль выше средней у {max_firm}, ниже среднней у {min_firm}')