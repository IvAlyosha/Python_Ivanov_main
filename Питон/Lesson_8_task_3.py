class Control_int(Exception):

    def __init__(self,value):
        self.value = value

    def add_list(self):
        if self.value.isdigit():
            return self.value
        else:
            while self.value.isalpha() or not self.value:
                self.value = input('Введите элемент списка (число)')
            return self.value

list_user = []
while True:
    user_date = input('Введите элемент списка, чтобы закончить введите stop')
    if user_date == 'stop':
        print(list_user)
        break
    try:
        raise Control_int(user_date)
    except Control_int as control:
        list_user.append(control.add_list())
