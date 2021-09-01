# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, matrix_item):
        self.matrix_item = matrix_item

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, matrix_row)) for matrix_row in self.matrix_item])

    def __add__(self, other):
        if len(self.matrix_item) != len(other.matrix_item) or len(self.matrix_item[0]) != len(other.matrix_item[0]):
            raise ValueError('Неверный размер матриц')
        result = []
        for i in range(len(self.matrix_item)):
            result.append([])
            for j in range(len(self.matrix_item[0])):
                result[i].append(self.matrix_item[i][j] + other.matrix_item[i][j])
        return '\n'.join(['\t'.join(map(str, result)) for result in result])


matrix1 = Matrix([[1, 2], [3, 4], [0, 5]])
print(matrix1, '\n')
matrix2 = Matrix([[5, 6], [7, 8], [3, 3]])
print(matrix2, '\n')
print(matrix1 + matrix2)
