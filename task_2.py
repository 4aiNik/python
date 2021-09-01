# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс)
# этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто
# и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть
# обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, dimensions):
        self.dimensions = dimensions

    @abstractmethod
    def calc_of_tissue_consumption(self):
        pass


class Coat(Clothes):
    @property
    def calc_of_tissue_consumption(self):
        return self.dimensions / 6.5 + 0.5


class Costume(Clothes):
    @property
    def calc_of_tissue_consumption(self):
        return 2 * self.dimensions + 0.3


coat = Coat(50)
result_1 = coat.calc_of_tissue_consumption
print(result_1)
costume = Costume(170)
result_2 = costume.calc_of_tissue_consumption
print(result_2)
print(result_1 + result_2)
