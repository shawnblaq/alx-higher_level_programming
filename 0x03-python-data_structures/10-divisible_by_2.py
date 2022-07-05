#!/usr/bin/python3

my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)

i = 0
while i < len(list_result):
    print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
    i += 1

def divisible_by_2(my_list=[]):
    new_list = []
    if my_list:
        for elm in my_list:
            new_list.append(False if elm % 2 else True)
    return new_list
