#4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
# возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания
# необходимо обойтись без встроенной функции возведения числа в степень.
def get_exponentiated_number():
    """
    Возведение в степень (2 способа)
    :return: float | none
    """
    result = None
    try:
        real_number = float(input('Действительное положительное число: '))
    except ValueError:
        print('Первое число не действительное')
        return result
    if real_number <= 0:
        print('Первое число не положительное')
        return result

    try:
        integer_number = int(input('Целое отрицательное число: '))
    except ValueError:
        print('Второе число не целое')
        return result
    if integer_number >= 0:
        print('Второе число не отрицательное')

    #Вариант 1 с **
    return real_number ** integer_number
    #либо Вариант 2 с циклом
    current_number = 1
    for i in range(abs(integer_number)):
        current_number *= real_number
    return 1 / current_number

result = get_exponentiated_number()
print(result)
