#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        maximo = -1000
        for i in my_list:
            if i > maximo:
                maximo = i
        return maximo
