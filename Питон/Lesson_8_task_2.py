class Err_proc(Exception):
    def __init__(self, txt):
        self.txt = txt

if __name__ == '__main__':
    while True:
        try:
            data_user_first_numb = int(input('Введите число'))
            data_user_second_numb = int(input('Введите 2ое число'))
            if data_user_second_numb == 0:
                raise Err_proc('divizion by zero')
            print(data_user_first_numb/data_user_second_numb)
        except Err_proc as err:
            print(err)
        except ValueError:
            print('Нужно ввести число')

