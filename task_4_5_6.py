# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
# в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

class Warehouse:
    def __init__(self):
        try:
            self.items
        except BaseException:
            self.items = {}

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Warehouse, cls).__new__(cls)
        return cls.instance

    def set_to_warehouse(self, object):
        current_type = object.__class__.__name__
        current_list = object.__dict__
        if current_type in self.items:
            if current_list['model'] in self.items[current_type]:
                self.items[current_type]['quantity'] += 1
            else:
                self.items[current_type][current_list['model']] = current_list
        else:
            current_key_dict = {}
            current_key_dict[current_list['model']] = current_list
            self.items[current_type] = current_key_dict

    def get_warehouse(self):
        try:
            self.items
        except BaseException:
            self.items = {}
        return self.items


class OfficeEquipment:
    def __init__(self, model, price, quantity):
        self.model = model
        self.price = price
        self.quantity = quantity
        self.validate_int()

    def take_to_warehouse(self, object):
        warehouse = Warehouse()
        warehouse.set_to_warehouse(object)

    def validate_int(self):
        try:
            self.price = int(self.price)
            self.quantity = int(self.quantity)
        except BaseException:
            raise ValueError('Ввод не верных данных в числовые поля!')


class Printer(OfficeEquipment):
    def __init__(self, model, price, quantity, color):
        super().__init__(model, price, quantity)
        self.color = color


class Scanner(OfficeEquipment):
    def __init__(self, model, price, quantity, max_resolution):
        super().__init__(model, price, quantity)
        self.max_resolution = max_resolution


class Xerox(OfficeEquipment):
    def __init__(self, model, price, quantity, print_speed):
        super().__init__(model, price, quantity)
        self.print_speed = print_speed


printer = Printer('Canon', 20000, 20, '5-color')
scanner = Scanner('Brother', 80000, 10, 'A4')
xerox = Xerox('Xerox', 12000, 15, 20)
printer.take_to_warehouse(printer)
printer.take_to_warehouse(scanner)
printer.take_to_warehouse(xerox)
warehouse = Warehouse()
print(warehouse.get_warehouse())
