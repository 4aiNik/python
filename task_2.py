# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.

class Division(Exception):
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    def divide(self):
        try:
            self.divider = int(self.divider)
            self.denominator = int(self.denominator)
            return self.divider / self.denominator
        except ZeroDivisionError:
            return 'На ноль делить нельзя'
        except ValueError:
            return 'Введено не число'
        except OwnError as err:
            return err


num_1 = input('Введите делимое: ')
num_2 = input('Введите делитель: ')
div = Division(num_1, num_2)
result = div.divide()
print(result)
