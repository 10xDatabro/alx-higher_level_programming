#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    new_dict = a_dictionary.copy()
    if key in new_dict.keys():
        new_dict[key] = value
    else:
        new_dict[key] = new_dict.get(key, value)
    return new_dict
