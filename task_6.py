# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день
# спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который общий
# результат спортсмена составить не менее b километров. Программа должна принимать значения параметров a и b и
# выводить одно натуральное число — номер дня.
first_day_distance = input('Ввести количество километров в первый день: ')
limit_distance = input('Ввести максимальное количество километров: ')
if not first_day_distance.isdigit() or not limit_distance.isdigit():
    print('Введено не числовое значение')
else:
    first_day_distance = int(first_day_distance)
    limit_distance = int(limit_distance)
    day = 1
    if first_day_distance < limit_distance:
        current_distance = 0
        while current_distance < limit_distance:
            if day == 1:
                current_distance = round(first_day_distance + first_day_distance / 10, 2)
            else:
                current_distance = round(current_distance + current_distance / 10, 2)
            day += 1

    print(f'Ответ: на {day}-й день спортсмен достиг результата — не менее {limit_distance} км.')
