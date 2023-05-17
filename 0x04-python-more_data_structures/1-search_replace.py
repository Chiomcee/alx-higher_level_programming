#!/usr/bin/python3

def search_replace(my_list, search, replace):
    # Create a new list with the same elements as the input list
    new_list = my_list[:]
    for n in range(len(new_list)):
        if new_list[n] == search:
            new_list[n] = replace
    return (new_list)
