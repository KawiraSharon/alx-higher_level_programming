#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """divide element by element 2 lists"""
    quotientList = []
    for idx in range(list_length):
        try:
            quotient = my_list_1[idx] / my_list_2[idx]
        except (TypeError):
            print("wrong type")
            quotient = 0
        except (ZeroDivisionError):
            print("division by 0")
            quotient = 0
        except (IndexError):
            print("out of range")
            quotient = 0
        finally:
            quotientList.append(quotient)
    return quotientList
