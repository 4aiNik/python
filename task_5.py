#5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться
# сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь
# введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ,
# выполнение программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить
# сумму этих чисел к полученной ранее сумме и после этого завершить программу.
result_sum = 0
while True:
    stop = False
    row_values = input('Ввод строки чисел с пробелами. q - конец ввода ')
    values = row_values.split(' ')
    for value in values:
        if value == 'q':
            stop = True
            break
        try:
            value = int(value)
        except Exception as e:
            print(f'Не целое число: {e}')
            continue
        result_sum += value
    print(f'Сумма: {result_sum}')
    if stop:
        break
