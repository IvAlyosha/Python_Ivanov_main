class Cell:
    def __init__(self,count_cell):
        self.count_cell = count_cell

    def __add__(self, other):
        return self.count_cell + other.count_cell

    def __sub__(self, other):
        if self.count_cell - other.count_cell < 0:
            print('Разность клеток не может быть меньше нуля')
        else: return self.count_cell - other.count_cell

    def __mul__(self, other):
        return self.count_cell * other.count_cell

    def __truediv__(self, other):
        return round(self.count_cell / other.count_cell)

    def make_round(self,count_cell_in_cell):
        string_cell = ''
        row = self.count_cell // count_cell_in_cell
        remains = self.count_cell % count_cell_in_cell
        print(remains)
        for count in range(row):
            string_cell = '*'*count_cell_in_cell+'\n'+string_cell
        if remains != 0:
            string_cell = string_cell + '\n' + (remains)*'*'+'.'*(count_cell_in_cell-remains)
        print(string_cell)

cell_1 = Cell(50)
cell_2 = Cell(157)
cell_2.make_round(3)