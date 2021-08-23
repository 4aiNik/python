# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

row_counter = 0
file = open('for_task_2.txt', 'r')
rows = file.readlines()
for row in rows:
    words_list = row.split()
    current_counter = len(words_list)
    row_counter += 1
    print(f'В {row_counter} строке {current_counter} слов')
file.close()
print(f'Всего строк: {row_counter}')
