#!/usr/bin/python3
def element_at(my_list, idx):
    if type(idx) is int:
        if idx < 0 or idx > len(my_list) or idx == len(my_list):
            return None
        else:
            return my_list[idx]
    else:
        return None
