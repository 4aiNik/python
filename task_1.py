# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего
# (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
# (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.

from time import sleep


class TrafficLight:
    __color = ('красный', 'желтый', 'зеленый')

    def running(self):
        counter = 0
        while True:
            index = counter % 3
            if index == 0:
                print("\033[31m {}" .format(TrafficLight.__color[index]))
                sleep(7)
            elif index == 1:
                print("\033[33m {}" .format(TrafficLight.__color[index]))
                sleep(2)
            elif index == 2:
                print("\033[32m {}" .format(TrafficLight.__color[index]))
                sleep(4)
            counter += 1


object = TrafficLight()
object.running()
