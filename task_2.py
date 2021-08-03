# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
input_seconds = input('Время в секундах: ')
if not input_seconds.isdigit():
    print('Введено не числовое значение')
else:
    hour = int(input_seconds) // 3600
    time_left_no_hour = int(input_seconds) - hour * 3600
    minutes = time_left_no_hour // 60
    seconds = time_left_no_hour - minutes * 60
    print(f'{hour:02}:{minutes:02}:{seconds:02}')
