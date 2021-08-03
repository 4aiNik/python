# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
number = input('Ввести число: ')
if not number.isdigit():
    print('Введено не числовое значение')
else:
    index = 0
    max_number = 0
    while index < len(number):
        current_number = int(number[index])
        if current_number > max_number:
            max_number = current_number
        index += 1
    print(f'результат:{max_number}')
