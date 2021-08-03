# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
number = input('Задуманное число: ')
if not number.isdigit():
    print('Введено не числовое значение')
else:
    number_2 = number + number
    number_3 = number_2 + number
    result = int(number) + int(number_2) + int(number_3)
    print(f'результат:{result}')
