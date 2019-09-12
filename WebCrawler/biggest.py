#!/usr/bin/env python3

"""
define a procedure that takes 3 numbers and inputs the greatest of the 3
"""


def biggest(x, y, z):
    if x > y:
        biggest = x
    else:
        biggest = y

    if biggest > z:
        return biggest
    else:
        return z

print(biggest(6, 2, 3))
print(biggest(6, 2, 7))
print(biggest(6, 9, 3))
