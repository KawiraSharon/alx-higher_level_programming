#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Prints x elements from list"""
    elementsPrinted = 0
    try:
        for idx in range(x):
            print("{}".format(my_list[idx]), end="")
            elementsPrinted += 1
        print()
        return elementsPrinted
    except IndexError:
        print()
        return elementsPrinted
