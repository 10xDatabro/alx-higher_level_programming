#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    new_list = my_list[::-1]
    for number in new_list:
        print("{:d}".format(number))
