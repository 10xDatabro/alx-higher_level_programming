#!/usr/bin/python3
def element_at(my_list, idx):
    val = 0
    if idx < 0 or idx > len(my_list):
        val = None
    else:
        val = my_list[idx]

    return val
