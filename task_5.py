# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

path = 'for_task_5.txt'
file_w = open(path, 'w')
text = input('Ввод чисел, разделенных пробелами: ')
file_w.write(text)
file_w.close()
file_r = open(path, 'r')
content = file_r.readline()
file_r.close()
items = content.split()
sum = 0
for item in items:
    if not item.isdigit():
        print('Введено не числовое значение')
    else:
        sum += int(item)
print(sum)
