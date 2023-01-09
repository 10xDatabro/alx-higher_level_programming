#!/usr/bin/python3
def max_integer(my_list=[]):
    if type(my_list) is list:
        largest_num = 0
        if len(my_list) == 0:
            largest_num = None
        for number in my_list:
            if largest_num < number:
                largest_num = int(number)
    return largest_num
