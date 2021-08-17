# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове
# функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел,
# начиная с 1! и до n!.
def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
        yield result


final = input('Ввод конечного числа: ')
if not final.isdigit():
    print('Не числовое значение')
else:
    for item in fact(int(final)):
        print(item)
