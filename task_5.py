# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает
# фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите
# численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
revenue = input('Выручка фирмы: ')
costs = input('Издержки фирмы: ')
if not revenue.isdigit() or not costs.isdigit():
    print('Введено не числовое значение')
else:
    revenue = int(revenue)
    costs = int(costs)
    if revenue > costs:
        print('Финансовый результат: прибыль')
        profitability = round((revenue - costs) / revenue, 2)
        print(f'Рентабельность: {profitability}')
        staff_number = int(input('Количество сотрудников: '))
        one_profit = round((revenue - costs) / staff_number, 2)
        print(f'Прибыль на одного сотрудника: {one_profit}')
    elif revenue < costs:
        print('Финансовый результат: убыток')
    else:
        print('Выручка и издержки равны')
