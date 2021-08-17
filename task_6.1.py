# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного
from itertools import count

start_num = input('Ввод первого числа: ')
final_num = input('Ввод последнего числа: ')
if not start_num.isdigit() or not final_num.isdigit():
    print('Не числовое значение')
else:
    start_num = int(start_num)
    final_num = int(final_num)
    for item in count(start_num):
        if item > final_num:
            break
        print(item)
