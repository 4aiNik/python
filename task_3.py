#3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
# (зима, весна, лето, осень). Напишите решения через list и через dict.
month_number = input('Месяц (число от 1 до 12): ')
if not month_number.isdigit():
    print('Введено не числовое значение')
elif int(month_number) < 1 or int(month_number) > 12:
    print('Введено не верное значение')
else:
    month_number = int(month_number)
    #вариант list
    seasons = ['', 'зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']
    print(seasons[month_number])
    #вариант dict
    seasons_2 = {
        1: 'зима', 2: 'зима', 12: 'зима',
        3: 'весна', 4: 'весна', 5: 'весна',
        6: 'лето', 7: 'лето', 8: 'лето',
        9: 'осень', 10: 'осень', 11: 'осень'
    }
    print(seasons_2[month_number])
