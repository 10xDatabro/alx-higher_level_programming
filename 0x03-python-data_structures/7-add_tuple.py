#!/usr/bin/python3
def create_list_of_lists(tuple_of_tuples=()):
    list_of_lists = []
    for t in tuple_of_tuples:
        list_of_lists.append(list(t))
    return list_of_lists


def create_matrix(list_of_lists=[]):
    row_num = len(list_of_lists)
    for i in range(row_num):
        cur_row = list_of_lists[i]
        col_num = len(cur_row)
        if col_num < 2:
            for i in range(2 - col_num):
                cur_row.append(0)
        if col_num > 2:
            del cur_row[2:]


def add_tuple(tuple_a=(), tuple_b=()):
    if type(tuple_a) is tuple and type(tuple_b) is tuple:
        tuple_pack = (tuple_a, tuple_b)
        list_of_lists = create_list_of_lists(tuple_pack)
        create_matrix(list_of_lists)
        add_1 = 0
        add_2 = 0
        for p in list_of_lists:
            a, b = p
            add_1 = add_1 + a
            add_2 = add_2 + b
    return (add_1, add_2)
