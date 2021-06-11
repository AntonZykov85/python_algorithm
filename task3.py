from random import randint

def top_profit1(): # O(n)
    sorted_dict = {}
    sorted_company = sorted(company, key=company.get, reverse=True)
    for v in sorted_company:
        sorted_dict[v] = company[v]
        top_profit = list(sorted_dict.items())[:3]
    print('компании с максимальной прибылью: ', top_profit)

def top_profit2(): # O(n^2)
    sorted_dict = {}
    sorted_company = sorted(company.values(), reverse=True)
    for i in sorted_company: # O(n)
        for keys in company.keys(): # O(n)
            if company[keys] == i:
                sorted_dict[keys] = company[keys]
        top_profit = list(sorted_dict.items())[:3]
    print('компании с максимальной прибылью: ', top_profit)



company = {'ланит' : randint(0,1000000),
           'фаргус' : randint(0,1000000),
           'аккела' : randint(0,1000000),
           'мэйл.ру' : randint(0,1000000),
           'яндекс' : randint(0,1000000)}

print(company)
top_profit1()
top_profit2()

# эффективнее будет вариант 1. и кода меньше