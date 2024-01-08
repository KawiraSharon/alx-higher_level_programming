#!/usr/bin/python3

def no_c(my_string):
    newstring = ""
    for idx in range(len(my_string)):
        if (my_string[idx] != 'c') and (my_string[idx] != 'C'):
            newstring += my_string[idx]
    return newstring