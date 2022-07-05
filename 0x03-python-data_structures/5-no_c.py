#!/usr/bin/env python3

print(no_c("Holberton School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))

def no_c(my_string):
    new_string = ""
    for c in my_string:
        if c != 'c' and c != 'C':
            new_string += c
    return new_string
