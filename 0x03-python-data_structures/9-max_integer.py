#!/usr/bin/python3

my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))

def max_integer(my_list=[]):
    if my_list:
        max = my_list[0]
        for elm in my_list:
            if elm > max:
                max = elm
        return max
    return Non
