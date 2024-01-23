#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tmp = ()
    for i in range(2):
        if i < len(tuple_a) and i < len(tuple_b):
            tmp += (tuple_a[i] + tuple_b[i],)
        elif i >= len(tuple_b) and i < len(tuple_a):
            tmp += (tuple_a[i],)
        elif i >= len(tuple_a) and i < len(tuple_b):
            tmp += (tuple_b[i],)
        else:
            tmp += (0, )
    return tmp
