#5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми
# значениями, то новый элемент с тем же значением должен разместиться после них.
list_length = input('Ввести количество элементов рейтинга: ')
if not list_length.isdigit():
    print('Введено не числовое значение')
else:
    index = 0
    list_length = int(list_length)
    custom_list = []
    while index < list_length:
        index += 1
        current_value = input('Ввод ' + str(index) + ' элемента рейтинга: ')
        if not current_value.isdigit():
            print('Введено не числовое значение')
            break
        current_value = int(current_value)
        custom_list.append(current_value)
        custom_list.sort(reverse=True)
        print(custom_list)
