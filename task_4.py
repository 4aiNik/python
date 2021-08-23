# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

file_data = open('for_task_4_data.txt', 'r')
file_result = open('for_task_4_result.txt', 'w')
dictionary = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}
rows = file_data.readlines()
for row in rows:
    row_list = row.split()
    row_list[0] = dictionary[row_list[0]]
    file_result.write(' '.join(row_list) + '\n')
file_data.close()
file_result.close()
