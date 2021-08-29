# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police
# (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение
# о превышении скорости.

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return 'Машина ' + self.name + ' поехала'

    def stop(self):
        return 'Машина ' + self.name + ' остановилась'

    def turn(self, direction):
        return 'Машина ' + self.name + ' повернула ' + direction

    def show_speed(self):
        return 'Текущая скорость: ' + self.speed


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return 'Превышение скорости: ' + str(self.speed)
        return 'Текущая скорость: ' + str(self.speed)


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return 'Превышение скорости: ' + str(self.speed)
        return 'Текущая скорость: ' + str(self.speed)


class PoliceCar(Car):
    pass


renault = TownCar(70, 'yellow', 'renault', False)
print(renault.go())
print(renault.turn('направо'))
print(renault.show_speed())
print(renault.stop())
