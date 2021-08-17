# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета для
# конкретных значений необходимо запускать скрипт с параметрами.
from sys import argv

try:
    output_in_hours = int(argv[1])
    rate_per_hour = int(argv[2])
    bonus = int(argv[3])
    print(output_in_hours * rate_per_hour + bonus)
except Exception as e:
    print(f'script error: {e}')
