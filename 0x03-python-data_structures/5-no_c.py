#!/usr/bin/python3
def no_c(my_string):
    tmp = ""
    for i in my_string:
        if i not in "cC":
            tmp += i
    return tmp
