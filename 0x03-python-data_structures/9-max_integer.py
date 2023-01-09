#!/usr/bin/python3
def max_integer(my_list=[]):
    largest_num = None
    if type(my_list) is list:
        if len(my_list) == 0:
            break
        for number in my_list:
            if largest_num is None or number > largest_num:
                largest_num = number
    return largest_num
