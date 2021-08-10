# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит
# информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно,
# т.е. запрашивать все данные у пользователя.
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.
def get_product_list():
    """
    Получение списка товаров
    :return: list
    """
    products = []
    products_length = input('Ввести количество товаров: ')
    if not products_length.isdigit():
        print('Введено не числовое значение')
        return products
    index = 0
    products_length = int(products_length)
    while index < products_length:
        all_parameters = input('Ввод параметров товаров через разделитель: название;цена;количество;единицы измерения ')
        all_parameters = all_parameters.split(';')
        if len(all_parameters) != 4:
            print('Введены не все параметры')
            continue
        if not all_parameters[1].isdigit():
            print('Цена - не числовое значение')
            continue
        if not all_parameters[2].isdigit():
            print('Количество - не числовое значение')
            continue
        index += 1
        single_dict = {
            'название': all_parameters[0],
            'цена': all_parameters[1],
            'количество': all_parameters[2],
            'ед': all_parameters[3]
        }
        single_tuple = (index, single_dict)
        products.append(single_tuple)
    return products


def get_product_analytics(products):
    """
    Сбор аналитики о товарах: словарь
    :param products: list
    :return: dict
    """
    results = {}
    fields = list(products[0][1].keys())
    for product in products:
        for title, value in product[1].items():
            for field in fields:
                if title != field:
                    continue
                results.setdefault(field, [])
                if value in results[field]:
                    continue
                results[field].append(value)
    return results


products = get_product_list()
if len(products) == 0:
    print('Нет товаров')
else:
    print(products)
    analytics = get_product_analytics(products)
    print(analytics)
