#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if len(my_list > 0):
        new_list = my_list.copy()
        new_list.reverse()
        for number in new_list:
            print("{:d}".format(number))
    else:
        return None
