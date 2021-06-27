from random import randint
from pympler import asizeof
from numpy import array
import json



def top_profit2(company):
    sorted_dict = {}
    sorted_company = sorted(company.values(), reverse=True)
    for i in sorted_company:
        for keys in company.keys():
            if company[keys] == i:
                sorted_dict[keys] = company[keys]
        top_profit = list(sorted_dict.items())[:3]
        return top_profit

def top_profit2_json(company):
    sorted_dict = {}
    sorted_company = sorted(company.values(), reverse=True)
    for i in sorted_company:
        for keys in company.keys():
            if company[keys] == i:
                sorted_dict[keys] = company[keys]
        top_profit = list(sorted_dict.items())[:3]
        json_d = json.dumps(sorted_dict)
        del sorted_dict
        return json_d

company = {'ланит' : randint(0,1000000),
           'фаргус' : randint(0,1000000),
           'аккела' : randint(0,1000000),
           'мэйл.ру' : randint(0,1000000),
           'яндекс' : randint(0,1000000)}


print(company)
print(asizeof.asizeof(top_profit2(company)))
print(asizeof.asizeof(top_profit2_json(company)))

"""Анализ: при выполнении сериализации словаря в json формат потребление памяти уменьшилось 
с 240 до 96
"""


