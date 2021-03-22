import random


class Storage:

    def __init__(self, name_storage, capacity):
        self.name_storage = name_storage
        self.capacity = capacity
        self.count_accepted_equipment = 0
        self.count_issued_equipment = 0
        self.storage = {
            'printer': [],
            'scanner': [],
            'xerox': [],
        }
        self.count_equipment = {
            'printer': 0,
            'scanner': 0,
            'xerox': 0,
        }

    def accepted_storage(self, data_equipment):
        print(self.count_accepted_equipment)
        self.data_equipment = data_equipment.__dict__
        if self.count_accepted_equipment - self.count_issued_equipment >= self.capacity:
            print('Склад заполнен')
        elif not self.data_equipment['manufacturers_name'] or not self.data_equipment['model'] or not \
        self.data_equipment['serial_number']:
            print('information is empty')
        else:
            self.count_accepted_equipment += 1
            self.storage[self.data_equipment['type_equipment']].append(self.data_equipment)
            self.count_equipment[self.data_equipment['type_equipment']] += 1
            print(self.storage)

    def issued_storage(self, type_equipment, model, office):
        i = 0
        for item in self.storage[type_equipment]:
            if item['manufacturers_name'] == model:
                self.storage[type_equipment].pop(i)
                self.count_issued_equipment += 1
                self.count_equipment[type_equipment] -= 1
                tracking_code = random.randint(100000000, 999999999)
                print(f'{type_equipment} {model} sent in {office}, tracking code:{tracking_code}')
                print(self.storage)
                print(self.count_equipment)
                break
            else:
                print('Такой модели нет')
            i += 1


class OfficeEquipment:
    def __init__(self, manufacturers_name, function, sheet_capacity, type_equipment, serial_number, model):
        self.manufacturers_name = manufacturers_name
        self.model = model
        self.serial_number = serial_number
        self.expendable_material = 'paper'
        self.power_supply = 220
        self.location_work = 'Chief office'
        self.function = function
        self.sheet_capacity = sheet_capacity
        self.type_equipment = type_equipment


class Printer(OfficeEquipment):
    def __init__(self, manufacturers_name, function, sheet_capacity, type_equipment, serial_number, model,
                 print_performance, paint_consumption):
        super().__init__(manufacturers_name, function, sheet_capacity, type_equipment, serial_number, model)
        self.print_performance = print_performance
        self.paint_consumption = paint_consumption


class Scanner(OfficeEquipment):
    def __init__(self, manufacturers_name, function, sheet_capacity, type_equipment, serial_number, model,
                 scan_quality):
        super().__init__(manufacturers_name, function, sheet_capacity, type_equipment, serial_number, model)
        self.scan_quality = scan_quality


class Xerox(OfficeEquipment):
    def __init__(self, manufacturers_name, function, sheet_capacity, type_equipment, serial_number, model,
                 paint_consumption, availability):
        super().__init__(manufacturers_name, function, sheet_capacity, type_equipment, serial_number, model)
        self.paint_consumption = paint_consumption
        self.availability = availability


print_1 = Printer('Canon', 'reproduction of documents', 400, 'printer', 'sn234097', 'mx-48r', 40, 500)
print_2 = Printer('hp', 'reproduction of documents', 1000, 'printer', 'sn0980000597', 'rhk8-500', 10, 300)
scanner_1 = Scanner('hp', 'copying a document', 50, 'scanner', 'sn0000008597', 'rhk8-500', 1)
xerox_1 = Xerox('hp', 'copying a document', 50, 'xerox', 'sn0000943597', 'fx8000-5', 1, '70%')
storage_1 = Storage('office equipment', 5)
storage_1.accepted_storage(print_1)
storage_1.accepted_storage(print_2)
storage_1.accepted_storage(scanner_1)
storage_1.accepted_storage(xerox_1)
storage_1.issued_storage('printer', 'Canon', 'support office')
storage_1.issued_storage('xerox', 'hp', 'Chief office')
