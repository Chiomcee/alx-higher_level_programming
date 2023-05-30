#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res = []
    for x in range(0, list_length):
        try:
            quotient = my_list_1[x] / my_list_2[x]
        except ZeroDivisionError:
            quotient = 0
            print("division by 0")
        except TypeError:
            quotient = 0
            print("wrong type")
        except IndexError:
            quotient = 0
            print("out of range")
        finally:
            res.append(quotient)
    return (res)
