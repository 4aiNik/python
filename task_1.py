# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать
# число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить
# валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных
# данных.

import re


class Date:
    def __init__(self, date_text):
        self.date_text = str(date_text)

    @classmethod
    def extract_date(cls, date_text):
        date_text = cls.validate_date(date_text)
        text = re.split('-', date_text)
        result = [int(item) for item in text]
        return result

    @staticmethod
    def validate_date(date_text):
        if re.search('^\d{1,2}-\d{1,2}-\d{4}$', date_text) is None:
            raise ValueError('Неправильный формат даты')
        text = re.split('-', date_text)
        if int(text[0]) < 1 or int(text[0]) > 31:
            raise ValueError('Неправильное значение дня')
        if int(text[1]) < 1 or int(text[1]) > 12:
            raise ValueError('Неправильное значение месяца')
        return date_text


today = Date('12-11-2011')
print(today.extract_date('12-11-2011'))
