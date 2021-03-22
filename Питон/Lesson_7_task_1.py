class Matrix:

    def __init__(self,list_list):
        self.matrix = [elm for str in list_list for elm in str]
        self.str_matrix = len(list_list)
        self.column_matrix = len(list_list[0])

    def __str__(self):
        matrix_view = ''
        count_matrix = 0
        for string in range(self.str_matrix):
            matrix_view = matrix_view + '\n'
            for column in range(self.column_matrix):
                matrix_view = matrix_view + ' ' + str(self.matrix[count_matrix])
                count_matrix += 1
        return matrix_view

    def __add__(self,other):
        new_matrix = []
        for elm in range(len(self.matrix)):
            new_matrix.append(self.matrix[elm]+other.matrix[elm])
        return new_matrix

matrix = Matrix([[10,20,10,40,60],[10,20,10,40,70],[10,20,10,40,80]])
matrix_2 = Matrix([[100,200,100,400,600],[10,20,10,40,70],[10,20,10,40,80]])
print(matrix)
new_matrix = matrix+matrix_2
print(new_matrix)