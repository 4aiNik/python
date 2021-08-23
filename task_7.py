# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма
# получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

import json

profit = {}
average_profit = []
file_r = open('for_task_7.txt', 'r')
rows = file_r.readlines()
file_r.close()
for row in rows:
    data = row.split()
    profit[data[0]] = int(data[2]) - int(data[3])
    if profit[data[0]] > 0:
        average_profit.append(profit[data[0]])
result = [profit, {'average_profit': round(sum(average_profit) / len(average_profit), 2)}]
print(result)
file_w = open('for_task_7.json', 'w')
json.dump(result, file_w)
file_w.close()
