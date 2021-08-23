# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет
# средней величины дохода сотрудников.

row_counter = 0
all_money = 0
file = open('for_task_3.txt', 'r')
rows = file.readlines()
for row in rows:
    try:
        row_list = row.split()
        surname = row_list[0]
        money = int(row_list[1])
    except Exception as e:
        print(f'script error: {e}')
        continue
    all_money += money
    if money < 20000:
        print(f'Сотрудник {surname} оклад {money}')
    row_counter += 1
file.close()
if row_counter == 0:
    print('Нет строк с данными')
else:
    average_total_profit = int(all_money / row_counter)
    print(f'Средний доход всех сотрудников: {average_total_profit}')
