#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_values = {x for x in my_list}
    add = 0
    for x in uniq_values:
        add += x
    return add
