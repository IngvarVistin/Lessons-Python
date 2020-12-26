class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        matr = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

        for i in range(len(self.list_1)):
            for j in range(len(self.list_2)):
                matr[i][j] = self.list_1[i][j] + self.list_2[i][j]
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))

my_matrix = Matrix([[10, 15, 20],
                    [23, 26, 29],
                    [42, 46, 52]],
                   [[15, 20, 10],
                    [20, 50, 100],
                    [22, 52, 101]])
print(my_matrix.__add__())