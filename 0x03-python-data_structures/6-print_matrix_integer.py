#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if type(matrix) is list:
        row_num = len(matrix)
        col_num = len(matrix[0])
        for i in range(row_num):
            cur_row = matrix[i]
            if col_num == 0:
                print("{}".format(""))
            if col_num > 0:
                for n in range(col_num):
                    if n < col_num - 1:
                        print("{:d}".format(cur_row[n]), end=" ")
                    if n == col_num - 1:
                        print("{:d}".format(cur_row[n]))
