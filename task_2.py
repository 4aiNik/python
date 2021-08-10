# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с
# индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().
def get_custom_list():
    """
    Получение списка элементов
    :return: list
    """
    custom_list = []
    list_length = input('Ввести длину списка: ')
    if not list_length.isdigit():
        print('Введено не числовое значение')
        return custom_list
    index = 0
    list_length = int(list_length)
    while index < list_length:
        index += 1
        current_value = input('Ввод ' + str(index) + ' элемента списка: ')
        custom_list.append(current_value)
    return custom_list


def replacing_list_items(custom_list):
    """
    Обмен значений элементов
    :param custom_list: list
    :return: list
    """
    index = 0
    len_list = len(custom_list)
    while index < len_list:
        if index >= len_list or index + 1 >= len_list:
            break
        current_text = custom_list[index]
        custom_list[index] = custom_list[index + 1]
        custom_list[index + 1] = current_text
        index += 2
    return custom_list


custom_list = get_custom_list()
if len(custom_list) == 0:
    print('Нет элементов в списке')
else:
    results = replacing_list_items(custom_list)
    print(results)
