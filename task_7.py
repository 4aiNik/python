# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте
# перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса
# (комплексные числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного
# результата.

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        return f'{self.real} + {self.imaginary} * i'

    def __add__(self, other):
        return f'Сумма равна: {self.real + other.real} + {self.imaginary + other.imaginary} * i'

    def __mul__(self, other):
        return f'Произведение равно: {self.real * other.real - (self.imaginary * other.imaginary)} +' \
               f' {self.imaginary * other.real} * i '


number_1 = ComplexNumber(5, 7)
number_2 = ComplexNumber(3, -2)
print(number_1)
print(number_1 + number_2)
print(number_1 * number_2)
