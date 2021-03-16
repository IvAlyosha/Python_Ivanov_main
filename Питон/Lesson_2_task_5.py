number_list = [7, 12, 3, 4, 2]
append_user = number_list.append(int(input('введите номер рейтинга')))
result_list = sorted(number_list, reverse=True)
print(result_list)