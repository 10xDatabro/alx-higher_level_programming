#!/usr/bin/python3
def no_c(my_string):
    if type(my_string) is str:
        letter_list = list(my_string)
        letter_list = [x for x in my_string if x not in "cC"]
        return "".join(letter_list)
