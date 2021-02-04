class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        for i in self.my_list:
            for my_matrix in i:
                print(f"{my_matrix:4}", end="")
            print()
        return ''

    def __add__(self, other):
        if len(self.my_list) == len(other.my_list):
            for i in range(len(self.my_list)):
                for t in range(len(other.my_list[i])):
                    try:
                        self.my_list[i][t] = self.my_list[i][t] + other.my_list[i][t]
                    except IndexError:
                        print('Матрицы разных размеров')
            return Matrix.__str__(self)
        else:
            print('Матрицы разных размеров')


matrix = Matrix([[1, 2, 7], [3, 4, 8], [5, 6, 9]])
new_matrix = Matrix([[2, 3, 8], [4, 5, 9], [6, 7, 7]])
print(matrix + new_matrix)
