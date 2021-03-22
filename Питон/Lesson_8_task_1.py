class Date:
    def __init__(self, date):
        self.date = str(date)

    @classmethod
    def parse_date(cls,date):
        date_list = [int(item) for item in date.replace('-', ' ').split()]
        return date_list
    @staticmethod
    def validate_date(date):
        if (Date.parse_date(date)[1] == 2 and Date.parse_date(date)[0] > 28) or (Date.parse_date(date)[0] > 31 and Date.parse_date(date)[1] != 2):
            print('Количество дней не соответствует календарю')
        elif Date.parse_date(date)[1] > 12:
            print('Превышено количество месяцев')
        elif Date.parse_date(date)[2] >21:
            print('Будущий год')
        else:
            print(Date.parse_date(date)[0],Date.parse_date(date)[1],Date.parse_date(date)[2])

Date.parse_date('12-03-21')
Date.validate_date('21-02-21')
