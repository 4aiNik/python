#2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.
def print_data(**data):
    """
    Вывод именованных аргументов
    :param data: dict
    """
    for title, value in data.items():
        print(f'{title}: {value}', end='; ')


print_data(name='Nik', surname='Nazarov', birth_year='1989', city='Saint Petersburg', email='afk@wtf.ru', phone='103')
