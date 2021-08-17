# 6. Реализовать два небольших скрипта:
# а) итератор, повторяющий элементы некоторого списка, определенного заранее
from itertools import cycle

my_list = [1, 52345, 6236, 65, 34, 6, 346]
index = 0
for item in cycle(my_list):
    index += 1
    if index > len(my_list):
        break
    print(item)
